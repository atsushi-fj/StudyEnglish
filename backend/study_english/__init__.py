import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecretkey"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"


def localize_callback(*args, **kwargs):
    return "このページにアクセスするには、ログインが必要です。"

login_manager.localize_callback = localize_callback

from sqlalchemy.engine import Engine
from sqlalchemy import event


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

from study_english.main.views import main  
from study_english.users.views import users
from study_english.wordbook.views import wordbook
from study_english.error_pages.handlers import error_pages

# app.register_blueprint(main)
# app.register_blueprint(users)
# app.register_blueprint(wordbook)
# app.register_blueprint(error_pages)

from flask_restful import Api
from study_english.api import LoginApi, LogoutApi, AccountApi, CreateBookApi, RegisterApi, UsersApi, WordBooksApi, ImageApi, WordsApi, WordApi
from flask_cors import CORS

CORS(app)
api = Api(app)
api.add_resource(LoginApi, "/login")
api.add_resource(LogoutApi, "/logout")
api.add_resource(RegisterApi, "/register")
api.add_resource(UsersApi, "/users")
api.add_resource(AccountApi, "/<int:user_id>/account")
api.add_resource(CreateBookApi, "/<int:user_id>/create_book")
api.add_resource(WordBooksApi, "/<int:user_id>/wordbooks")
api.add_resource(ImageApi, "/images/<string:filename>")
api.add_resource(WordsApi, "/<int:wordbook_id>/words")
api.add_resource(WordApi, "/<int:wordbook_id>/word")
