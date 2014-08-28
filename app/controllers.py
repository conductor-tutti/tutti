#-*-coding:utf-8-*-
from app import app, db
from sqlalchemy import desc
from app.models import Article, Comment, User, Musician, Awards
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import ArticleForm, CommentForm, UserForm, LoginForm
from flask import jsonify, render_template, session, request, redirect, url_for, flash, g

@app.before_request
def before_request():
    g.username = None
    if "username" in session:
        g.username = session["username"]

@app.route('/', methods=["GET"])
def article_list():
    context = {}
    context["article_list"] = Article.query.order_by(desc(Article.date_created)).limit(1)
    return render_template("home.html", context=context, active_tab="article_list")

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
            return redirect(url_for("article_list"))

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
        return redirect(url_for("article_list"))

@app.route("/musician/musician_new/", methods=["GET", "POST"])
def musician_new():
    if request.method == "GET":
        return render_template("musician/musician_new.html")
    elif request.method == "POST":
        musician_id = session["user_id"]
        musician = Musician()
        awards = Awards(
            name = request.form.get("award_info"),
            musician = Musician.query.get(musician_id)
            )
        db.session.add(awards)
        db.session.commit()
        flash(u"존나좋군?")
        return redirect(url_for("article_list"))
        

@app.route('/user/sign_up', methods = ['GET', 'POST'])
def sign_up():
    form = UserForm()
    if request.method == 'GET':
        return render_template('user/sign_up.html', active_tab = 'sign_up', form = form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if db.session.query(User).filter(User.email == form.email.data).count() > 0:
                flash(u"이미 가입한 이메일입니다.", "danger")
                return render_template("user/sign_up.html", form=form, active_tab="sign_up")
            else:
                article_data = request.form
                user = User(
                    email=form.email.data,
                    password=generate_password_hash(form.password.data),
                    username=form.username.data
                )
                db.session.add(user)
                db.session.commit()
                flash(u"가입 완료!", "success")
                return redirect(url_for('sign_up_success', id = user.id))
    return render_template('user/sign_up.html', active_tab = 'sign_up', form = form)


@app.route('/sign_up_success/<int:id>', methods = ['GET'])
def sign_up_success(id):
    user = User.query.get(id)
    return render_template('user/sign_up_success.html', user=user)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template("login.html", active_tab="login", form=form)
    else:
        if form.validate_on_submit():
            userdata = User.query.filter(User.email == form.login_email.data).first()
            if userdata:
                if check_password_hash(userdata.password, form.login_password.data):
                    user_email = form.login_email.data
                    flash(u"반갑습니다, %s 님!" % userdata.username)
                    session["user_id"] = userdata.id
                    session["user_email"] = user_email
                    return redirect(url_for("article_list"))
                else:
                    flash(u"비밀번호가 다릅니다.", "danger")
                    return redirect(url_for("login", form=form))
            else:
                flash(u"존재하지 않는 이메일입니다.", "danger")
                return redirect(url_for("login", form=form))
        else:
            return render_template("login.html", active_tab="login", form=form)

@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    flash(u"잘가요, %s 님!" % g.username)
    return redirect(url_for("article_list"))


@app.route("/delete_account", methods=["GET", "POST"])
def delete_account():
    if request.method == "GET":
        return render_template("leave.html")
    elif request.method == "POST":
        user_id = session['user_id']
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()

        flash(u"게시글 지웠다능..ㅠㅠ", "success")
        return redirect(url_for("article_list"))