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
    # post = db.relationship("BlogPost", backref="author", lazy="dynamic")
    
    def __init__(self, email, username, password, administrator):
        self.email = email
        self.username = username
        self.password = password
        self.administrator = administrator
    
    def __repr__(self):
        return f"UserName: {self.username}"
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
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