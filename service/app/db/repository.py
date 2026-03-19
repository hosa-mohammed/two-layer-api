def insert_user(user):
    return {
        "message": "User inserted (fake)",
        "data": {
            "name": user.name,
            "email": user.email
        }
    }