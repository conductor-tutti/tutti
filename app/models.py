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

class Musician(db.Model):
    m_id = db.Column(db.Integer, primary_key=True)
    m_category = db.Column(db.String(20))
    m_major = db.Column(db.String(20))
    m_phrase = db.Column(db.String(50))
