from flask import request
from flask_restful import Resource, reqparse
from study_english.models import User
from flask_login import login_user, logout_user, login_required, current_user

class UserApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("email", required=True, help="Email cannot be blank")
        self.parser.add_argument("password", required=True, help="Password cannot be blank")
                
    def get(self):
        args = self.parser.parse_args()
        user = User.query.filter_by(email=args["email"]).first()
        if user and user.checkpassword(args["password"]):
            login_user(user)
            return {"message": "Login successful"}, 200
        return {"message": "Invalid credentials"}, 401
    
        
        