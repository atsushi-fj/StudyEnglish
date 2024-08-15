from flask import request
from flask_restful import Resource, reqparse
from study_english.models import User, WordBook, Word
from flask_login import login_user, logout_user, login_required, current_user
from study_english.image_handler import add_featured_image
import json
from flask import jsonify
from study_english import db
from flask import current_app, send_from_directory
import os

class LoginApi(Resource):
    
    def post(self):
        try: 
            data = request.get_json()
            user = User.query.filter_by(email=data["email"]).first()
            if user is not None:
                if user.check_password(data["password"]):
                    login_user(user)
                    return {"status": "SUCCESS", "id": str(user.id), "admin": str(user.is_administrator())}
                else:
                    return {"status": "PASSWORD FAIL"}
            return {"status": "USER FAIL"}
        except Exception as e:
            return {"status": "ERROR"}
        
class LogoutApi(Resource):
    
    @login_required
    def post(self):
        logout_user()
        return 
        
class RegisterApi(Resource):
    
    def post(self):
        try:
            data = request.get_json()
            if User.query.filter_by(username=data['username']).first():
                return {"status": "USESRNAME FAIL"}
            if User.query.filter_by(email=data['email']).first():
                return {"status": "EMAIL FAIL"}
            user = User(email=data['email'], username=data['username'],
                        password=data['password'], administrator="0")
            db.session.add(user)
            db.session.commit()
            return {"status": "SUCCESS"}
        except Exception as e:
            return {"status": "ERROR"}

class UsersApi(Resource):
    
    def get(self):
        try:
            page = int(request.args.get("page", 1))
            per_page = int(request.args.get("per_page", 10))
            users = User.query.paginate(page, per_page, False)
            return {
                "total": users.total,
                "pages": users.pages,
                "current_page": users.page,
                "per_page": users.per_page,
                "users": [user.to_dict() for user in users.items]                
            }
        except:
            return {"status": "ERROR"}
               
                                
class AccountApi(Resource):
    
    def get(self, user_id):
        try:
            user = User.query.get(user_id)
            return {
                "email": user.email,
                "username": user.username,
            }
        except:
            return {"status": "ERROR"}
    
    def put(self, user_id):
        try:
            data = request.get_json()
            user = User.query.get(user_id)
            if User.query.filter_by(username=data['username']).first():
                return {"status": "USESRNAME FAIL"}
            if User.query.filter_by(email=data['email']).first():
                return {"status": "EMAIL FAIL"}
            user.email = data["email"]
            user.username = data["username"]
            user.password = data["password"]
            db.session.commit()
            return {"status": "SUCCESS"}
        except:
            return {"status": "ERROR"}
        
    def delete(self, user_id):
        try:
            user = User.query.get(user_id)
            db.session.delete(user)
            db.session.commit()
            return {"status": "SUCCESS"}
        except:
            return {"status": "ERROR"}
        
   

class CreateBookApi(Resource):
    
    def put(self, user_id):
        try:
            title = request.form.get("title")
            picture = request.files["picture"]
            if picture:
                pic = add_featured_image(picture)
            else:
                pic = ""
            wordbook = WordBook(title=title, featured_image=pic,
                                user_id=user_id)
            db.session.add(wordbook)
            db.session.commit()
            return {"status": "Create successful"}
        except:
            return {"status": "FAIL"}

 
class WordBooksApi(Resource):
    
    def get(self, user_id):
        try:
            page = int(request.args.get("page", 1))
            per_page = int(request.args.get("per_page", 10))
            wordbooks = WordBook.query.filter_by(user_id=user_id).order_by(
                WordBook.id.desc()).paginate(page, per_page, False)
            return {
                "total": wordbooks.total,
                "pages": wordbooks.pages,
                "current_page": wordbooks.page,
                "per_page": wordbooks.per_page,
                "wordbooks": [wordbook.to_dict() for wordbook in wordbooks.items],
            }
        except:
            return {"status": "ERROR"}
        
    def delete(self, user_id):
        try:
            data = request.get_json()
            book = WordBook.query.get(data["book_id"])
            db.session.delete(book)
            db.session.commit()
            return {"status": "SUCCESS"}
        except:
            return {"status": "ERROR"}
        

  
class ImageApi(Resource):
    
    def get(self, filename):
        try:
            folder = os.path.join(current_app.root_path, r"static/featured_image")
            return send_from_directory(folder, filename)
        except:
            return {"status": "ERROR"}


class WordsApi(Resource):
    
    def get(self, wordbook_id):
        try:
            page = int(request.args.get("page", 1))
            per_page = int(request.args.get("per_page", 10))
            words = Word.query.filter_by(book_id=wordbook_id).order_by(
                Word.id.desc()).paginate(page, per_page, False)
            return {
                "total": words.total,
                "pages": words.pages,
                "current_page": words.page,
                "per_page": words.per_page,
                "words": [word.to_dict() for word in words.items],
            }
        except:
            return {"status": "ERROR"}

      
class WordApi(Resource):
    
    def put(self, wordbook_id):
        try:
            data = request.get_json()
            word = Word(japanese=data["japanese"], english=data["english"], book_id=wordbook_id)
            db.session.add(word)
            db.session.commit()
            return {"status": "Create successful"}
        except:
            return {"status": "FAIL"}
        
    def delete(self, wordbook_id):
        try:
            data = request.get_json()
            word = Word.query.get(data["word_id"])
            db.session.delete(word)
            db.session.commit()
            return {"status": "SUCCESS"}
        except:
            return {"status": "ERROR"}
        
