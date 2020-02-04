from . import create_app
from flask_script import Manager

app = create_app()
manager = Manager(app)


@manager.command
def dev():
    from livereload import Server
    server = Server(app.wsgi_app)
    server.watch("**/*.*")
    server.serve(open_url=True)


if __name__ == '__main__':
    manager.run()
