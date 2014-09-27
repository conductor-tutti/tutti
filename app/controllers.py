#-*-coding:utf-8-*-
from app import app, db, facebook, google
from sqlalchemy import desc, asc
from app.models import User, Musician, Category, Location, UserRelationship, Comment
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, make_response, render_template, session, request, redirect, url_for, flash, g
from google.appengine.api import images
from google.appengine.ext import blobstore
from werkzeug.http import parse_options_header
from datetime import timedelta
import re
import json
import logging
import os.path
import sys
reload(sys)

sys.setdefaultencoding('UTF8')

DB_INITIAL_DIRECTORY = './initial_data'

@app.before_request
def before_request():
    #category_list = ["클래식", "국악", "재즈", "실용음악", "기타 "]
    if db.session.query(Category).count() == 0:
        f = open(os.path.dirname(__file__) + DB_INITIAL_DIRECTORY + '/' + 'category_v1.csv')
        for line in f.readlines():
            logging.info(line)
            fields = line.split(',')
            category_record = Category(name=fields[1], upper_id=fields[2]) # Should not run twice because of auto increment id field
            db.session.add(category_record)
        f.close()
        db.session.commit()

    if db.session.query(Location).count() == 0:
        f = open(os.path.dirname(__file__) + DB_INITIAL_DIRECTORY + '/' + 'location_v1.csv')
        for line in f.readlines():
            fields = line.split(',')
            location_record = Location(name=fields[1], upper_id=fields[2]) # Should not run twice because of auto increment id field
            db.session.add(location_record)
        f.close()
        db.session.commit()

    
    g.userdata = None
    if 'user_id' in session:
        g.userdata = User.query.get(session["user_id"]) # FIX: It should be cached later on for prevention of unnecessary overhead on DB 

@app.route('/', methods=["GET"])
def index():
    index = {}
    musicians = Musician.query.order_by(desc(Musician.created_on)).limit(4)
    for musician in musicians:
        musician.profile_image = images.get_serving_url(musician.photo)
    index["musician_list"] = musicians
    return render_template("index.html", index=index, active_tab="index")


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
                session["user_id"] = userdata.id
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
    flash(u"%s 님, 다음에 또 만나요!" % g.userdata.username)
    return redirect(url_for("index"))

@app.route("/musician/musician_new/", methods=["GET", "POST"])
def musician_new():
    categories = Category.query.all()
    locations = Location.query.all()
    if session:
        user_id = session['user_id']

        target_url = "/musician/musician_new/"
        if request.method == "GET":
            upload_uri = blobstore.create_upload_url(target_url)

            musician = {}
            if g.userdata.is_musician == 1:
                musician_query = Musician.query.filter(Musician.user_id == user_id)
                musician = musician_query.first()

            return render_template("/musician/musician_new.html", target_url=target_url, profile_data=musician, upload_uri=upload_uri, categories=categories, locations=locations, active_tab="musician_new")

        elif request.method == "POST":
            photo = request.files["profile_image"]
            header = photo.headers["Content-Type"]
            parsed_header = parse_options_header(header)
            blob_key = None
            if(parsed_header[1].has_key("blob-key")):
                blob_key = parsed_header[1]["blob-key"]  

            #User.query.get(user_id)
            if g.userdata.is_musician == 0: # New musicion   
                musician = Musician(
                    user_id = user_id,
                    category_id = request.form.get("major"),
                    phrase = request.form.get("phrase"),
                    education = request.form.get("education"),
                    repertoire = request.form.get("repertoire"),
                    location_id = request.form.get("sigungu"),
                    photo = blob_key
                    )
                db.session.add(musician)
                flash(u"프로필이 잘 등록되었어요!", "success")
            else:
                musician_query = Musician.query.filter(Musician.user_id == user_id)
                musician = musician_query.first()

                category_id = request.form.get("major")
                if category_id != 'none':
                    musician.category_id = category_id 
                musician.phrase = request.form.get("phrase")
                musician.education = request.form.get("education")
                musician.repertoire = request.form.get("repertoire")

                location_id = request.form.get("location")
                if location_id != 'none':
                    musician.location_id = request.form.get("sigungu")


                # Delete old photo if photo has been updated
                if (blob_key != None) and (musician.photo != blob_key):
                    if musician.photo: # In case there is no photo
                        blobstore.delete(musician.photo)

                musician.photo = blob_key                
                flash(u"프로필이 잘 변경되었어요!", "success")

            db.session.commit()
        return redirect(url_for("index"))

    else:
        flash(u"로그인 후 이용해 주세요~", "danger")
        return redirect(url_for('index'))


@app.route("/musician/musician_location/", methods=["GET","POST"])
def musician_location():
    if request.method == "POST":
        locationsidoid = request.form.get("location")
        locations = Location.query.filter(Location.upper_id==locationsidoid).all()
        sigungu = {"locations":[(x.id, x.name) for x in locations]}
        return jsonify(sigungu)


@app.route("/musician/musician_category/", methods=["GET","POST"])
def musician_category():
    if request.method == "POST":
        categoryid = request.form.get("category")
        categories = Category.query.filter(Category.upper_id==categoryid).all()
        major = {"categories":[(x.id, x.name) for x in categories]}
        return jsonify(major)


@app.route("/musician/classic_musician/", methods=["GET"])
def classic_musician():
    category_list = Category.query.all()
    index = {}
    index["musician_list"] = Musician.query.order_by(desc(Musician.created_on)).filter(Musician.category_id == 1).limit(4)
    return render_template("musician/classic_musician.html", index=index, category_list=category_list, active_tab="index")


@app.route("/musician/<int:musician_id>", methods=["GET", "POST"])
def musician_profile(musician_id):
    musician = Musician.query.get(musician_id)
    user = User.query.get(musician.user_id)
    category_list = Category.query.all()
    username = user.username
    comments = musician.comments.order_by(asc(Comment.created_on)).all()
    return render_template("musician/profile.html", username=username, musician=musician, comments=comments)


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


@app.route('/facebook_login')
def facebook_login():
    return facebook.authorize(callback = url_for('facebook_authorized',
        next = request.args.get('next') or request.referrer or None,
        _external = True))

@app.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return redirect(url_for('index'))
    session['oauth_token'] = (resp['access_token'], '')
    me = facebook.get('/me')
    userdata = User.query.filter(User.facebook_id == me.data['id']).first()
    
    if userdata:
        session["user_email"] = userdata.email
        session["user_name"] = userdata.username
        session["user_id"] = userdata.id
        flash(u"반갑습니다, %s 님!" % session["user_name"])
    else:
        user = User(
                email = me.data['email'],
                username = me.data['name'],
                facebook_id = me.data['id'],
                access_token = session['oauth_token'][0],
                photo = 'http://graph.facebook.com/'+me.data['id']+'/picture/'
            )
        db.session.add(user)
        db.session.commit()
        userdata = User.query.filter(User.facebook_id == me.data['id']).first()
        session["user_email"] = userdata.email
        session["user_name"] = userdata.username
        session["user_id"] = userdata.id
        flash(u"반갑습니다, %s 님!" % session["user_name"])

    return redirect(url_for('index'))
    # return str(me.data)


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')


# This is login using google account
@app.route('/google_login')
def google_login():
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('login_go'))
 
    access_token = access_token[0]
    from urllib2 import Request, urlopen, URLError
 
    headers = {'Authorization': 'OAuth ' + access_token}
    req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                  None, headers)
    try:
        res = urlopen(req)
    except URLError, e:
        if e.code == 401:
            # Unauthorized - bad token
            session.pop('access_token', None)
            return redirect(url_for('login_go'))
        return res.read()
    google_userinfo = json.loads(res.read())
    userdata = User.query.filter(User.google_id == google_userinfo['id']).first()
    
    if userdata:
        session["user_email"] = userdata.email
        session["user_name"] = userdata.username
        session["user_id"] = userdata.id
        flash(u"반갑습니다, %s 님!" % session["user_name"])
    else:
        user = User(
                email = google_userinfo['email'],
                username = google_userinfo[u'name'],
                google_id = google_userinfo['id'],
                access_token = session['access_token'][0],
                photo = google_userinfo['picture']
            )
        db.session.add(user)
        db.session.commit()
        userdata = User.query.filter(User.google_id == google_userinfo['id']).first()
        session["user_email"] = userdata.email
        session["user_name"] = userdata.username
        session["user_id"] = userdata.id
        flash(u"반갑습니다, %s 님!" % session["user_name"])

    return redirect(url_for('index'))
    # return str(session['access_token'][0])
    # return str(google_userinfo)


@app.route('/login_go')
def login_go():
    callback = url_for('authorized', _external=True)
    return google.authorize(callback=callback)
 
 
@app.route('/login_go/authorized')
@google.authorized_handler
def authorized(resp):
    access_token = resp['access_token']
    session['access_token'] = access_token, ''
    return redirect(url_for('google_login'))
 
 
@google.tokengetter
def get_access_token():
    return session.get('access_token')


@app.route('/search_name', methods = ['GET','POST'])
def search_name():
    index = {}
    if request.method == "POST":
        index['userdata'] = User.query.filter(User.username.contains(request.form.get("search-name"))).limit(4)
        return render_template("show_friends.html", index=index, active_tab="index")


@app.route('/friendship_request/<int:user_id>', methods = ['GET', 'POST'])
def friendship_request(user_id):
    if request.method == "GET":
        userrelationship = UserRelationship(
            related_user = User.query.get(user_id),
            user = User.query.get(session["user_id"])
            )
        db.session.add(userrelationship)
        db.session.commit()
        flash(u"친구요청 되었습니다.", "success")
        return redirect(url_for('index'))
    elif request.method == "POST":
        return render_template("show_friends.html", index=index, active_tab="index")


@app.route('/my_friends', methods = ['GET','POST'])
def my_friends():
    index = {}
    index['friends_request'] = []
    index['friends'] = []
    index['request_friends'] = []
    friends_request = UserRelationship.query.filter(UserRelationship.type == 0, UserRelationship.user_id == session["user_id"]).all()
    friends = UserRelationship.query.filter(UserRelationship.type == 1, UserRelationship.user_id == session["user_id"]).all()
    request_friends = UserRelationship.query.filter(UserRelationship.type == 0, UserRelationship.related_user_id == session["user_id"]).all()
    for row in friends_request:
        user = User.query.get(row.related_user_id)
        index['friends_request'].append(user)
    for row in friends:
        user = User.query.get(row.related_user_id)
        index['friends'].append(user)
    for row in request_friends:
        user = User.query.get(row.user_id)
        index['request_friends'].append(user)
    return render_template("my_friends.html", index=index, active_tab="friend")


@app.route('/accept_friend_request/<int:user_id>', methods = ['GET', 'POST'])
def accept_friend_request(user_id):
    if request.method == "GET":
        userrelationship = UserRelationship(
            related_user = User.query.get(user_id),
            user = User.query.get(session["user_id"]),
            type = 1
             )
        existing_row = UserRelationship.query.filter(UserRelationship.user_id == user_id, UserRelationship.related_user_id == session["user_id"]).first()
        existing_row.type = 1
        db.session.add(userrelationship)
        db.session.commit()
        flash(u"친구가 되었습니다.", "success")
        return redirect(url_for('my_friends'))
    elif request.method == "POST":
        return render_template("show_friends.html", index=index, active_tab="index")


@app.route("/user_profile", methods=["GET", "POST"])
def user_profile():
    if session:
        user_id = session['user_id']
        if request.method == "GET":
            return render_template("user_profile.html", active_tab="user_profile")

    else:
        flash(u"로그인 후 이용해 주세요~", "danger")
        return redirect(url_for('index'))

@app.route("/comment_create", methods=["GET", "POST"])
def comment_create():
    if request.method == "POST":
        musician_id = request.form.get("musician_id_data")
        comment = Comment(
            author_name=g.userdata.username,
            content=request.form.get("comment_data"),
            musician=Musician.query.get(musician_id),
            user=User.query.get(session["user_id"])
        )
        db.session.add(comment)
        db.session.commit()
        data={"comment_data":request.form.get("comment_data"),"author_name":g.userdata.username,"success" : True}
        return jsonify(data)

