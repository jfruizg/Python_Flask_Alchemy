from flask import Flask
from routes.user import contact
from routes.comment import comment
from routes.excel import excel
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
local = Flask(__name__)

CAPTCHA_CONFIG = {'SECRET_CAPTCHA_KEY': 'wMmeltW4mhwidorQRli6Oijuhygtfgybunxx9VPXldz'}
local.secret_key = 'my_secret_key'

local.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:felipe1972@localhost/api_flask'
local.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://bab79d65de65fd:2089d769@us-cdbr-east-05.cleardb.net/heroku_f4bb183c903f077'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)
SQLAlchemy(local)

app.register_blueprint(contact)
local.register_blueprint(contact)
local.register_blueprint(comment)
local.register_blueprint(excel)


