from app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text())
    author = db.Column(db.String(255))
    category = db.Column(db.String(255))
    date_created = db.Column(db.DateTime(), default=db.func.now())

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"))
    article = db.relationship("Article",
        backref=db.backref("comments", cascade="all, delete-orphan", lazy="dynamic"))
    author = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    content = db.Column(db.Text())
    date_created = db.Column(db.DateTime(), default=db.func.now())


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    username = db.Column(db.String(255))    
    is_musician = db.Column(db.Integer, default=0)
    is_out = db.Column(db.Integer, default=0)
    

class Musician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User",
        backref=db.backref("musician", cascade="all, delete-orphan", lazy="dynamic"))
    category_id = db.Column(db.String(255))
    major_id = db.Column(db.String(255))
    phrase = db.Column(db.String(255))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    musicians = db.relationship("Musician", backref="category", lazy="dynamic")

class Major(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    musicians = db.relationship("Musician", backref="major", lazy="dynamic")
