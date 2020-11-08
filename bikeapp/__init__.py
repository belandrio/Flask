from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '57411af3803d40de9186755d5c9ba1c4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bike.db'
db = SQLAlchemy(app)

from bikeapp import routes