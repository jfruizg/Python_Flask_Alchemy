from flask import Flask
from routes.contact import contact
from routes.category import task
from flask_sqlalchemy import SQLAlchemy

prod = Flask(__name__)
local = Flask(__name__)

local.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:felipe1972@localhost/api_flask'
local.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

prod.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://bab79d65de65fd:2089d769@us-cdbr-east-05.cleardb.net/heroku_f4bb183c903f077'
prod.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(prod)
SQLAlchemy(local)

prod.register_blueprint(contact)
local.register_blueprint(contact)

prod.register_blueprint(task)
local.register_blueprint(task)