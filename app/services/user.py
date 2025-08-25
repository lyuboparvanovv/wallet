from db.database import get_db
from models.user import User
from schemas.user import CreateUser, UpdateUser
from sqlalchemy.orm import joinedload

def create_user(user: CreateUser):
    with get_db() as db:
        user_exist = db.query(User).filter_by(username=user.username).first()
        if user_exist:
            return None

        current_user = User(
            username=user.username,
            password=user.password,
            phone_number=user.phone_number,
            email=user.email,
            is_admin=False
        )

        db.add(current_user)
        db.commit()
        db.refresh(current_user)

        return current_user


def get_user(username: str):
    with get_db() as db:
        user = db.query(User).filter_by(username=username).first()

        if not user:
            return None

        return user

def update_user(username: str, updated_user: UpdateUser):

    with get_db() as db:

        user = db.query(User).filter_by(username=username).first()
        if not user:
            return None

        if updated_user.password is not None:
            user.password = updated_user.password
        if updated_user.phone_number is not None:
            user.phone_number = updated_user.phone_number
        if user.email is not None:
            user.email = updated_user.email

        db.commit()
        db.refresh(user)

        return user

def get_user_with_cards(user_id):

    with get_db() as db:
        user = db.query(User).options(joinedload(User.cards)).filter_by(id=user_id).first()

        return user

def add_money(username, amount: float):

    with get_db() as db:
        user = db.query(User).filter_by(username=username).first()

        user.money += amount

        db.commit()
        db.refresh(user)

        return user