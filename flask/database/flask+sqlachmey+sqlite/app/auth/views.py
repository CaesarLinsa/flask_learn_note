# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from flask import Blueprint
from flask_login import login_user, logout_user, current_user
from .forms import LoginForm
from ..models import User, Role
from .. import db

auth = Blueprint('auth', __name__)


@auth.route("/")
def index():
    return render_template("index.html", title="hello world")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate():
        user = User.query.filter_by(name=form.username.data, password=form.password.data).first()
        if user is not None:
            login_user(user)
            return redirect(url_for('auth.index'))

    return render_template('login.html',
                           title=u'登录',
                           form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/about')
def about():
    return render_template('about.html', title=u'关于')
