from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask_oauth import OAuth
from app import settings

GOOGLE_CLIENT_ID = '446320683721-5682au4ts51jm1al7rhf3fmlp8l5btid.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'hWYMEa07SuVQ5WeLkAjCVwAU'

SECRET_KEY = 'YOUWILLNEVERKNOWTHISKEY'
DEBUG = True

app = Flask(__name__)
app.config.from_object("app.settings.Production")
app.debug = DEBUG
app.secret_key = SECRET_KEY

oauth = OAuth()

google = oauth.remote_app('google', 
    base_url='https://www.google.com/accounts/',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    request_token_url=None,
    request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email', 'response_type': 'code'},
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_method='POST',
    access_token_params={'grant_type': 'authorization_code'},
    consumer_key=GOOGLE_CLIENT_ID,
    consumer_secret=GOOGLE_CLIENT_SECRET)

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=settings.Production.FACEBOOK_APP_ID,
    consumer_secret=settings.Production.FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
    )

db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)

from app import controllers, models
