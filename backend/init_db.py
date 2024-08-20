from study_english import app
from study_english import db
from study_english.models import User

with app.app_context():
    db.drop_all()
    db.create_all()
    user1 = User(email="admin_user@test.com", username="Admin User",
                password="123", administrator="1")
    db.session.add(user1)
    db.session.commit()