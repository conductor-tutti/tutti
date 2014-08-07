from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager


app = Flask(__name__)
app.config.from_object("app.settings.Production")

db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)

from app import controllers, models
