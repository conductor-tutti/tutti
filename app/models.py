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
    userid = db.Column(db.String(15))
    password = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))

class MusicianCategory(db.Model):
    id = db.Column(db.Interger, primary_key = True)
    name = db.Column(db.String(40))

class MusicianMajor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))

class Musician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("MusicianCategory.id"))
    major_id = db.Column(db.Integer, db.ForeignKey("MusicianMajor.id"))
    phrase = db.Column(db.String(50))
