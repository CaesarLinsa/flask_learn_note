from flask import render_template, request, redirect, url_for, render_template_string
from flask import Blueprint
from ..models import Article, Comment, Reply
from .forms import ArticleForm, CommentForm, ReplyForm
from flask_login import login_required, current_user
from .. import db

main = Blueprint('main', __name__)


@main.route("/")
def index():
    return render_template("index.html", title="caesar博客")


@main.route('/article/<int:id>', methods=['GET', 'POST'])
def comments(id):
    article = Article.query.get_or_404(id)
    form = CommentForm(request.form)
    # 保存评论
    if form.validate_on_submit():
        comment = Comment(body=form.body.data, article_id=id, auther_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for(".comments", id=id))
    return render_template("article/details.html",
                           title=article.title,
                           form=form,
                           article=article)


@main.route('/edit', methods=['GET', 'POST'])
@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id=0):
    form = ArticleForm(request.form)
    if form.validate_on_submit():
        if id == 0:
            article = Article(user=current_user)
        else:
            article = Article.query.get_or_404(id)
        article.body = form.body.data
        article.title = form.title.data

        db.session.add(article)
        db.session.commit()
        # url_for调用处理函数函数名
        return redirect(url_for('.comments', id=article.id))

    title = u'添加文章'
    if id > 0:
        article = Article.query.get_or_404(id)
        form.body.data = article.body
        form.title.data = article.title
        title = u'编辑%s' % article.title

    return render_template('article/edit.html',
                           title=title,
                           form=form)


@main.route('/reply/<int:article_id>/<int:comment_id>', methods=['GET', 'POST'])
@login_required
def reply(article_id, comment_id):
    form = ReplyForm(request.form)
    if form.validate_on_submit():
        reply = Reply(comment_id=comment_id,auther_id=current_user.id)
        reply.body = form.body.data
        db.session.add(reply)
        db.session.commit()
        # url_for调用处理函数函数名
        return redirect(url_for('.comments', id=article_id))
    return render_template("article/reply.html", form=form)


@main.route('/about')
def about():
    return render_template('about.html', title=u'关于')
