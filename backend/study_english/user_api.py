from flask import request, jsonify
from flask_restful import Resource
from study_english.models import User
from study_english import db


class LoginApi(Resource):
    
    def post(self):
        try: 
            data = request.get_json()
            user = User.query.filter_by(email=data["email"]).first()
            if user is not None:
                if user.check_password(data["password"]):
                    return {"status": "SUCCESS",
                            "id": str(user.id),
                            "admin": str(user.is_administrator()),
                            "username": str(user.username)}
                else:
                    return {"status": "PASSWORD FAIL"}
            return {"status": "USER FAIL"}
        except:
            return {"status": "ERROR"}


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
        except:
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
