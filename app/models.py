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
    photo = db.Column(db.String(255))
    # just forget deleting accounts until 'real' launching
    ## is_out = db.Column(db.Integer, default=0)    


class Musician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))
    user = db.relationship("User",
        backref=db.backref("musician", cascade="all, delete-orphan", lazy="dynamic"))
    
    category_upper_id = db.Column(db.Integer, db.ForeignKey("category.id")) # big class level 
    category_id = db.Column(db.Integer, db.ForeignKey("category.id")) # smaller class level
    category = db.relationship("Category", foreign_keys=[category_id], backref=db.backref("musician", cascade="all, delete-orphan", lazy="dynamic"))
    
    location_upper_id = db.Column(db.Integer, db.ForeignKey("location.id"))
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"))
    location = db.relationship("Location", foreign_keys=[location_id], backref=db.backref("musician", cascade="all, delete-orphan", lazy="dynamic"))
    
    phrase = db.Column(db.String(255))
    photo = db.Column(db.String(255)) # blob key lives in here
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    upper_id = db.Column(db.Integer)


class Education(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    musician_id = db.Column(db.Integer, db.ForeignKey("musician.id"))
    musician = db.relationship("Musician",
        backref=db.backref("educations", cascade="all, delete-orphan", lazy="dynamic"))
    education_data = db.Column(db.String(255))
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


class Repertoire(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    musician_id = db.Column(db.Integer, db.ForeignKey("musician.id"))
    musician = db.relationship("Musician",
        backref=db.backref("repertoires", cascade="all, delete-orphan", lazy="dynamic"))
    repertoire_data = db.Column(db.String(255))
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


class Video(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    musician_id = db.Column(db.Integer, db.ForeignKey("musician.id"))
    musician = db.relationship("Musician",
        backref=db.backref("videos", cascade="all, delete-orphan", lazy="dynamic"))
    video_data = db.Column(db.String(255))
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    upper_id = db.Column(db.Integer)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    musician_id = db.Column(db.Integer, db.ForeignKey("musician.id"))
    author_name = db.Column(db.String(255))
    content = db.Column(db.Text())
    is_out = db.Column(db.Integer, default=0)
    user = db.relationship("User", foreign_keys=[user_id])
    musician = db.relationship("Musician",
        backref=db.backref("comments", cascade="all, delete-orphan", lazy="dynamic"))
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
