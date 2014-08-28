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
    

class Musician(User):
    category = db.Column(db.Integer)
    major = db.Column(db.Integer)
    phrase = db.Column(db.String(255))


class Awards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    musician_id = db.Column(db.Integer, db.ForeignKey("musician.id"))
    musician = db.relationship("Musician", backref=db.backref("awards", lazy="dynamic"))


# class MusicianCategory(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(40), default="(classic), (jazz)")
#     musicians = db.relationship("Musician", backref="category", lazy="dynamic")

# class MusicianMajor(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(40))
#     musicians = db.relationship("Musician", backref="major", lazy="dynamic")
