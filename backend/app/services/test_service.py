from app.database.models import TestUser

def create_test_user(db, name):
    user = TestUser(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user