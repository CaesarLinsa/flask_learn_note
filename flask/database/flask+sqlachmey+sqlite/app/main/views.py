from flask import render_template, request
from flask import Blueprint

main = Blueprint('main', __name__)


@main.route("/")
def index():
    return render_template("index.html", title="hello world")


@main.route('/login', methods=["GET", "POST"])
def login():
    from app.auth.forms import LoginForm
    form = LoginForm()
    if request.method == "POST":
        form_obj = LoginForm(request.form)
        if form_obj.validate():
            ers = request.form.to_dict()
            print(ers)
            print(form_obj.data)
            return "登录成功"
    return render_template("login.html", form=form)


@main.route('/about')
def about():
    return render_template('about.html', title=u'关于')
