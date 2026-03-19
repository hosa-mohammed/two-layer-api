from app.db.repository import insert_user

def create_user(user):
    return insert_user(user)