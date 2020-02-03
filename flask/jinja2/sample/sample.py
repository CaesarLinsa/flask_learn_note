# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask_script import Manager
from livereload import Server
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

app = Flask(__name__)
manager = Manager(app)
Bootstrap(app)
nav = Nav()

nav.register_element('top', Navbar('Flask入门',
                                   View('主页', 'index'),
                                   View('登录', 'login')
                                   ))
nav.init_app(app)


@app.route("/")
def index():
    return render_template("index.html", title="hello world")


@app.route('/login', methods=["GET", "POST"])
def login():
    from forms import LoginForm
    form = LoginForm()
    if request.method == "POST":
        form_obj = LoginForm(request.form)
        if form_obj.validate():
            ers = request.form.to_dict()
            print(ers)
            print(form_obj.data)
            return "登录成功"
    return render_template("login.html", form=form)


if __name__ == '__main__':
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url_delay=True)
