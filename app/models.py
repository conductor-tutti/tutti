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

    # just forget deleting accounts until 'real' launching
    ## is_out = db.Column(db.Integer, default=0)
    

class Musician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User",
        backref=db.backref("musician", cascade="all, delete-orphan", lazy="dynamic"))
    
    # each musician has its own category_id
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category = db.relationship("Category", backref=db.backref("category", cascade="all, delete-orphan", lazy="dynamic"))
    
    # and major_id too
    major_id = db.Column(db.Integer, db.ForeignKey("major.id"))
    major = db.relationship("Major", backref=db.backref("major", cascade="all, delete-orphan", lazy="dynamic"))
    phrase = db.Column(db.String(255))
    date_created = db.Column(db.DateTime(), default=db.func.now())
    
    # Soyoung'll initialize Location table
    ## location_id = db.Column(db.Integer, db.ForeignKey("location.id"))
    ## location = db.relationship()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    
    # musicians have same category_id will be updated in this column
    musicians = db.relationship("Musician")

class Major(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    
    # each major has its mother category
    category_id = db.Column(db.Integer)
    
    # same as musicians in Category table
    musicians = db.relationship("Musician")
