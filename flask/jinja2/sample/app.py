from flask import Flask, render_template, request, redirect, url_for, abort
import logging
from utils import log_utils
from os import path
from flask_script import Manager

log_utils.setup(level=logging.DEBUG,
                outs=[log_utils.RotatingFile(filename="caesar.log",
                                             level=logging.DEBUG,
                                             max_size_bytes=100000,
                                             backup_count=3)],
                program_name=None,
                capture_warnings=True)

LOG = logging.getLogger(__name__)
app = Flask(__name__)
manager = Manager(app)


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        LOG.info("username is :%s and password is %s" % (username, password))
    else:
        return render_template("login.html", method=request.method)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    try:
        if request.method == "POST":
            f = request.files.get('file')
            basepath = path.abspath(path.dirname(__name__))
            upload_path = path.join(basepath, "static", "uploads")
            if not path.exists(upload_path):
                LOG.error("%s is not exist" % upload_path)
            f.save(upload_path + "/" + f.filename)
            return redirect(url_for('upload'))
        else:
            return render_template("upload.html")
    except Exception as e:
        LOG.error("upload caught an exception :%s" % str(e))
        abort(500)


@app.errorhandler(500)
def inner_error(error):
    return render_template("500.html"), 500


if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
