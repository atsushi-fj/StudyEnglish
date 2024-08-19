import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecretkey"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

from sqlalchemy.engine import Engine
from sqlalchemy import event


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

from flask_restful import Api
from study_english.user_api import LoginApi, AccountApi, RegisterApi, UsersApi
from study_english.wordbook_api import CreateBookApi, WordBooksApi, ImageApi, WordsApi, WordApi, AllWordsApi, SpeakApi, PublicWordBooksApi, WordBookApi
from flask_cors import CORS

CORS(app)
api = Api(app)
api.add_resource(LoginApi, "/login")
api.add_resource(SpeakApi, "/speak")
api.add_resource(RegisterApi, "/register")
api.add_resource(UsersApi, "/users")
api.add_resource(AccountApi, "/<int:user_id>/account")
api.add_resource(CreateBookApi, "/<int:user_id>/create_book")
api.add_resource(WordBooksApi, "/<int:user_id>/wordbooks")
api.add_resource(ImageApi, "/images/<string:filename>")
api.add_resource(WordsApi, "/<int:wordbook_id>/words")
api.add_resource(WordApi, "/<int:wordbook_id>/word")
api.add_resource(AllWordsApi, "/<int:wordbook_id>/all_words")
api.add_resource(WordBookApi, "/<int:wordbook_id>/get_wordbook_id")
api.add_resource(PublicWordBooksApi, "/public_wordbooks")
