# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from os import path

base_url = path.abspath(path.dirname(__name__))
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)

    Bootstrap(app)

    app.config.from_pyfile('config')
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + path.join(base_url, "data.sqlite")
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    db.init_app(app)
    login_manager.init_app(app)
    from .auth.views import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    from .main.views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @app.template_test('current_link')
    def is_current_link(link):
        return link == request.path

    return app
