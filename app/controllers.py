#-*-coding:utf-8-*-
from app import app, db
from sqlalchemy import desc
from app.models import Article
from flask import render_template, request, redirect, url_for, flash


@app.route('/', methods=["GET"])
def article_list():
    context = {}
    context["article_list"] = Article.query.order_by(desc(Article.date_created)).all()
    return render_template("home.html", context=context, active_tab="article_list")

@app.route("/article/create/", methods=["GET", "POST"])
def article_create():
    if request.method == "GET":
        return render_template("article/create.html", active_tab="article_create")

    elif request.method == "POST":
        article_data = request.form
        article = Article(
            title=article_data.get("title"),
            author=article_data.get("author"),
            category=article_data.get("category"),
            content=article_data.get("content")
        )
        db.session.add(article)
        db.session.commit()
        flash(u"게시물이 작성되따능.", "success")
        return redirect(url_for("article_list"))
