#-*-coding:utf-8-*-
from app import app, db
from sqlalchemy import desc
from app.models import Article, Comment, User, Musician, Category, Major
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import ArticleForm, CommentForm
from flask import jsonify, make_response, render_template, session, request, redirect, url_for, flash, g
from google.appengine.api import images
from werkzeug.http import parse_options_header
from google.appengine.ext import blobstore
import logging

@app.before_request
def before_request():
    category_list = ["클래식", "국악"]
    if db.session.query(Category).count() == 0:
        for category in category_list:
            category_record = Category(name=category)
            db.session.add(category_record)
        db.session.commit()
    
    g.username = None
    if 'user_name' in session:
        g.username = session["user_name"]
        
@app.route('/', methods=["GET"])
def index():
    index = {}
    index["musician_list"] = Musician.query.order_by(desc(Musician.created_on)).limit(4)
    return render_template("index.html", index=index, active_tab="index")

@app.route("/total_article_num")
def total_article_num():
    article_num = db.session.query(Article).count()
    return jsonify(article_num=article_num)

@app.route("/more_article")
def more_article():
    current_row = int(request.args.get("current_row"))
    article_num = int(request.args.get("article_num"))
    more_article = db.session.query(Article).order_by(desc(Article.date_created))[current_row:current_row+1]
    data = {}
    data["article"] = []
    temp = {}
    for article in temp["title"]: 
        temp["id"] = article.id
        temp["title"] = article.title
        temp["content"] = article.content
        temp["author"] = article.author
        temp["category"] = article.category
        temp["date_created"] = article.date_created

        data["article"].append(temp)
        temp = {}
    return jsonify(data)

@app.route("/article/create/", methods=["GET", "POST"])
def article_create():
    form = ArticleForm()
    if request.method == "GET":
        return render_template("article/create.html", form=form, active_tab="article_create")
    elif request.method == "POST":
        if form.validate_on_submit():
            article = Article(
                title=form.title.data,
                author=form.author.data,
                category=form.category.data,
                content=form.content.data
            )
            db.session.add(article)
            db.session.commit()
            flash(u"게시물이 작성되따능.", "success")
            return redirect(url_for("index"))

@app.route("/article/detail/<int:article_id>", methods=["GET"])
def article_detail(article_id):
    article = Article.query.get(article_id)
    comments = article.comments.order_by(desc(Comment.date_created)).all()
    return render_template("article/detail.html", article=article, comments=comments)


@app.route("/comment/create/<int:article_id>", methods=["GET", "POST"])
def comment_create(article_id):
    form = CommentForm()
    if request.method == "GET":
        return render_template("article/create.html", form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            comment = Comment(
                author=form.author.data,
                email=form.email.data,
                content=form.content.data,
                password=form.password.data,
                article=Article.query.get(article_id)
            )
            db.session.add(comment)
            db.session.commit()
            flash(u"댓글 작성해따능.", "success")
            return redirect(url_for("article_detail", id=article_id))
        return render_template("article/create.html", form=form)

@app.route("/article/update/<int:article_id>", methods=["GET", "POST"])
def article_update(article_id):
    article = Article.query.get(article_id)
    form = ArticleForm(request.form, obj=article)
    if request.method == "GET":
        return render_template("article/update.html", form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            form.populate_obj(article)
            db.session.commit()
            return redirect(url_for("article_detail", article_id=article_id))
        return render_template("article/update.html", form=form)

@app.route("/article/delete/<int:article_id>", methods=["GET", "POST"])
def article_delete(article_id):
    if request.method == "GET":
        return render_template("article/delete.html", article_id=article_id)
    elif request.method == "POST":
        article_id = request.form["article_id"]
        article = Article.query.get(article_id)
        db.session.delete(article)
        db.session.commit()

        flash(u"게시글 지웠다능..ㅠㅠ", "success")
        return redirect(url_for("index"))


@app.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html', active_tab = 'sign_up')
    elif request.method == 'POST':     
        if db.session.query(User).filter(User.email == request.form.get("user-email")).count() > 0:
            flash(u"이미 가입한 이메일입니다.", "danger")
            return render_template("sign_up.html", active_tab="sign_up")
        else:
            user = User(
                email = request.form.get("user-email"),
                password = generate_password_hash(request.form.get("user-pw")),
                username = request.form.get("user-name"),
            )
            db.session.add(user)
            db.session.commit()
            flash(u"가입이 완료되었습니다. 반가워요!", "success")
            return redirect(url_for('index'))
        return render_template('sign_up.html', active_tab='sign_up')


@app.route('/sign_up_success/<int:id>', methods = ['GET'])
def sign_up_success(id):
    user = User.query.get(id)
    return render_template('user/sign_up_success.html', user=user)

@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template("sign_in.html", active_tab="sign_in")
    else:
        userdata = User.query.filter(User.email == request.form.get("user-email")).first()
        if userdata:
            if check_password_hash(userdata.password, request.form["user-pw"]):
                flash(u"반갑습니다, %s 님!" % userdata.username)
                session["user_id"] = userdata.id
                session["user_email"] = userdata.email
                session["user_name"] = userdata.username
                return redirect(url_for("index"))
            else:
                flash(u"비밀번호가 다릅니다.", "danger")
                return redirect(url_for("sign_in"))
        else:
            flash(u"존재하지 않는 이메일입니다. 정확히 입력하셨나요?", "danger")
            return redirect(url_for("sign_in"))
    
@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    flash(u"%s 님, 다음에 또 만나요!" % g.username)
    return redirect(url_for("index"))

@app.route("/musician/musician_new/", methods=["GET", "POST"])
def musician_new():
    user_id = session['user_id']
    upload_uri = blobstore.create_upload_url("/musician/musician_new/")
    if request.method == "GET":
        category = Category.query.all()
        major = Major.query.all()
        return render_template("/musician/musician_new.html", upload_uri=upload_uri, category=category, major=major, active_tab="musician_new")
    elif request.method == "POST":
        photo = request.files["profile_image"]
        header = photo.headers["Content-Type"]
        parsed_header = parse_options_header(header)
        blob_key = parsed_header[1]["blob-key"]
        User.query.get(user_id).is_musician = 1
        musician = Musician(
            user_id = user_id,
            category_id = request.form.get("category"),
            major_id = request.form.get("major"),
            phrase = request.form.get("phrase"),
            photo = blob_key
            )
        db.session.add(musician)
        db.session.commit()
        flash(u"프로필이 잘 등록되었어요!", "success")
        return redirect(url_for("index"))

@app.route("/musician/<int:musician_id>", methods=["GET", "POST"])
def musician_profile(musician_id):
    musician = Musician.query.get(musician_id)
    user = User.query.get(musician.user_id)
    username = user.username
    return render_template("musician/profile.html", username=username, musician=musician)

@app.route("/photo/get/<path:blob_key>/", methods=["GET"])
def get_photo(blob_key):
    if blob_key:
        blob_info = blobstore.get(blob_key)
        logging.warn(blob_info)
        if blob_info:
            img = images.Image(blob_key=blob_key)
            img.im_feeling_lucky()
            thumbnail = img.execute_transforms(output_encoding=images.PNG)
            logging.info(thumbnail)

            response = make_response(thumbnail)
            response.headers["Content-Type"] = blob_info.content_type
            return response

@app.route('/photo/resized/<path:blob_key>/', methods=['GET'])
def get_resized_photo(blob_key):
    if blob_key:
        blob_info = blobstore.get(blob_key)
        logging.warn(blob_info)
        if blob_info:
            img = images.Image(blob_key=blob_key)
            img.resize(width=250, height=250)
            img.im_feeling_lucky()
            thumbnail = img.execute_transforms(output_encoding=images.PNG)
            logging.info(thumbnail)

            response = make_response(thumbnail)
            response.headers['Content-Type'] = blob_info.content_type
            return response
