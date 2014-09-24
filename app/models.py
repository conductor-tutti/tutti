from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    username = db.Column(db.String(255))    
    is_musician = db.Column(db.Integer, default=0)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    access_token = db.Column(db.String(255))
    facebook_id = db.Column(db.String(255))
    google_id = db.Column(db.String(255))

    # just forget deleting accounts until 'real' launching
    ## is_out = db.Column(db.Integer, default=0)    

class Musician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))
    user = db.relationship("User",
        backref=db.backref("musicians_user", cascade="all, delete-orphan", lazy="dynamic"))

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category = db.relationship("Category", backref=db.backref("musician", cascade="all, delete-orphan", lazy="dynamic"))

    major_id = db.Column(db.Integer, db.ForeignKey("major.id"))
    major = db.relationship("Major", backref=db.backref("musician", cascade="all, delete-orphan", lazy="dynamic"))

    location_id = db.Column(db.Integer, db.ForeignKey("location.id"))
    location = db.relationship("Location", backref=db.backref("musician", cascade="all, delete-orphan", lazy="dynamic"))

    phrase = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


class Major(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category = db.relationship("Category", backref=db.backref("categorys_major", cascade="all, delete-orphan", lazy="dynamic"))

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


class UserRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User",
        backref=db.backref("userrelationship", cascade="all, delete-orphan", lazy="dynamic"))
    relateduserid = db.Column(db.Integer)
    type = db.Column(db.Integer, default=0)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


class Location(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    upper_id = db.Column(db.Integer)
   

