# app/app.py

#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)
_
db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555)