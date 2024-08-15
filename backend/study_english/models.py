from datetime import datetime
from pytz import timezone
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from study_english import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    administrator = db.Column(db.String(1))
    book = db.relationship("WordBook", backref="author", lazy="dynamic")
    
    def __init__(self, email, username, password, administrator):
        self.email = email
        self.username = username
        self.password = password
        self.administrator = administrator
    
    def __repr__(self):
        return f"UserName: {self.username}"
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "administrator": self.administrator,
        }
    
    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def is_administrator(self):
        if self.administrator == "1":
            return 1
        else:
            return 0


class WordBook(db.Model):
    __tablename__ = "wordbook"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    date = db.Column(db.DateTime, default=datetime.now(timezone("Asia/Tokyo")))
    title = db.Column(db.String(140))    
    featured_image = db.Column(db.String(140))
    word = db.relationship("Word", backref="word", lazy="dynamic")
    
    def __init__(self, title, featured_image, user_id):
        self.title = title
        self.featured_image = featured_image
        self.user_id = user_id
    
    def __repr__(self):
        return f"PostID: {self.id}, Title: {self.title}, Author: {self.author} \n"
    
    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date.isoformat(),
            "title": self.title,
            "image": str(self.featured_image),
        }
    
    
class Word(db.Model):
    __tablename__ = "word"
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("wordbook.id"))
    english = db.Column(db.String[140])
    japanese  = db.Column(db.String[140])
    
    def __init__(self, english, japanese, book_id):
        self.english = english
        self.japanese = japanese
        self.book_id = book_id
        
    def __repr__(self):
        return f"WordID: {self.id}, EnglishWord: {self.english}, JapaneseWord: {self.japanese} \n"
    
    def to_dict(self):
        return {
            "id": self.id,
            "english": self.english,
            "japanese": self.japanese,
        }
    