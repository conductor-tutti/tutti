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
        backref=db.backref("musician", cascade="all, delete-orphan", lazy="dynamic"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category = db.relationship("Category", backref=db.backref("musician", cascade="all, delete-orphan", lazy="dynamic"))
    
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"))
    location = db.relationship("Location", backref=db.backref("musician", cascade="all, delete-orphan", lazy="dynamic"))

    phrase = db.Column(db.String(255))
    education = db.Column(db.String(255))
    repertoire = db.Column(db.String(255))
    photo = db.Column(db.String(255)) # blob key lives in here

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    upper_id = db.Column(db.Integer)


class UserRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    related_user_id = db.Column(db.Integer, db.ForeignKey("user.id")) 
    type = db.Column(db.Integer, default=0)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    user = db.relationship("User", foreign_keys=[user_id])
    related_user = db.relationship("User", foreign_keys=[related_user_id])

    
class Location(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    upper_id = db.Column(db.Integer)
