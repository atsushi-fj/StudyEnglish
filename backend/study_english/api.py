from flask import request
from flask_restful import Resource, reqparse
from study_english.models import User
from flask_login import login_user, logout_user, login_required, current_user
import json
from flask import jsonify
from study_english import db

class LoginApi(Resource):
    def post(self):
        try: 
            data = request.get_json()
            user = User.query.filter_by(email=data["email"]).first()
            if user is not None:
                if user.check_password(data["password"]):
                    login_user(user)
                    return {"status": "SUCCESS"}
                else:
                    return {"status": "PASSWORD FAIL"}
            return {"status": "USER FAIL"}
        except Exception as e:
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
        except Exception as e:
            return {"status": "ERROR"}
                    


class CreateBookApi(Resource):
    
    def put(self, user_id):
        title = request.args.get["title"]
        if title:
            return title
        return {"message": "Create successful"}, 200
    
        
        