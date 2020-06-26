from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
# https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()