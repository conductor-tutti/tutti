#-*-coding:utf-8-*-
from app import app, db, facebook, google
from sqlalchemy import desc
from app.models import User, Musician, Category, Major
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import MusicianProfileForm
from flask import jsonify, make_response, render_template, session, request, redirect, url_for, flash, g
from google.appengine.api import images
from werkzeug.http import parse_options_header
from google.appengine.ext import blobstore
from datetime import timedelta

import re
import json
import logging
import sys
reload(sys)
sys.setdefaultencoding('UTF8')
# give app.secret_key the same value with SECRET_KEY in Config in settings.py
app.secret_key = "xrdtfvbyuhnjimuygtfrdessdfnhhmjjygh65hrytrytr"

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


@app.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html', active_tab = 'sign_up')
    elif request.method == 'POST':     
        if db.session.query(User).filter(User.email == request.form.get("user-email")).count() > 0:
            flash(u"이미 가입한 이메일입니다.", "danger")
            return render_template("sign_up.html", active_tab="sign_up")
        else:
            if len(request.form.get('user-pw'))<8 or re.match("^[a-zA-Z0-9 ]+$", request.form.get('user-pw')):
                flash(u"비밀번호를 8자 이상, 특수문자를 포함해주세요!", "danger")
                return render_template("sign_up.html", active_tab="sign_up") 
                # print "..boo"
            else:
                # print "OK!"
                user = User(
                    email = request.form.get("user-email"),
                    password = generate_password_hash(request.form.get("user-pw")),
                    username = request.form.get("user-name")
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
                access_token = session['oauth_token'][0]
            )
        db.session.add(user)
        db.session.commit()
        userdata = User.query.filter(User.facebook_id == me.data['id']).first()
        session["user_email"] = userdata.email
        session["user_name"] = userdata.username
        session["user_id"] = userdata.id
        flash(u"반갑습니다, %s 님!" % session["user_name"])

    return redirect(url_for('index'))

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
                access_token = session['access_token'][0]
            )
        db.session.add(user)
        db.session.commit()

        userdata = User.query.filter(User.googleogle_id == google_userinfo['id']).first()
        session["user_email"] = userdata.email
        session["user_name"] = userdata.username
        session["user_id"] = userdata.id
        flash(u"반갑습니다, %s 님!" % session["user_name"])

    return redirect(url_for('index'))
    # return str(session['access_token'][0])
    
 
 
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
