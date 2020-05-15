from questionary import create_app, db
from questionary.models import *

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()