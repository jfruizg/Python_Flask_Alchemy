from flask import Flask
from routes.contact import contact
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://b56a86448bafb:bf464afa@us-cdbr-east-05.cleardb.net/heroku_71115a8dcdb2348'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(contact)