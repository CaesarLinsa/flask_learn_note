from . import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from . import db

app = create_app()
manager = Manager(app)
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
