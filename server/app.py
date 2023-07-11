# server/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)

db.init_app(app)


if __name__ == '__main__':
    app.run(port=5555, debug=True)




##"Scan not a friend with a microscopic glass / You know his faults, now let his foibles pass 
# / Life is one long enigma, my friend / So read on, read on, the answer's at the end."