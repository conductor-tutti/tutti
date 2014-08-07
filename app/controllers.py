#-*-coding:utf-8-*-
from app import app, db
from sqlalchemy import desc
from app.models import Article, Comment
from flask import render_template, request, redirect, url_for, flash
from app.forms import ArticleForm, CommentForm


@app.route('/', methods=["GET"])
def article_list():
    context = {}
    context["article_list"] = Article.query.order_by(desc(Article.date_created)).all()
    return render_template("home.html", context=context, active_tab="article_list")

@app.route("/article/create/", methods=["GET", "POST"])
def article_create():
    form = ArticleForm()
    if request.method == "GET":
        return render_template("article/create.html", form=form, active_tab="article_create")
    elif request.method == "POST":
        if form.validate_on_submit():
            article = Article(
                title=form.title.data,
                author=form.author.data,
                category=form.category.data,
                content=form.content.data
            )
            db.session.add(article)
            db.session.commit()
            flash(u"게시물이 작성되따능.", "success")
            return redirect(url_for("article_list"))
