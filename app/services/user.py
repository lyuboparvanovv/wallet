from db.database import get_db
from models.user import User
from schemas.card import CardOut
from schemas.user import CreateUser, UpdateUser, TransactionOut, UserWholeInfo, FriendsOut
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

def get_user_whole_info(user_id):

    with (get_db() as db):
        user = db.query(User).options(
            joinedload(User.cards),
            joinedload(User.friends)
        ).filter_by(id=user_id).first()

        transactions = []

        for t in user.sent_transactions:
            receiver = db.query(User).get(t.receiver_id)
            transactions.append(TransactionOut(
                sender=user.username,
                receiver=receiver.username if receiver else "Unknown",
                amount=t.amount,
                date=t.date
            ))

        for t in user.received_transactions:
            sender = db.query(User).get(t.sender_id)
            transactions.append(TransactionOut(
                sender=sender.username if sender else "Unknown",
                receiver=user.username,
                amount=t.amount,
                date=t.date
            ))

        return UserWholeInfo(
            username=user.username,
            password=user.password,
            email=user.email,
            phone_number=user.phone_number,
            money=user.money,
            is_admin=user.is_admin,
            cards=[CardOut.from_orm(card) for card in user.cards],
            friends=[FriendsOut.from_orm(friend) for friend in user.friends],
            transactions=transactions
        )

def add_money(username, amount: float):

    with get_db() as db:
        user = db.query(User).filter_by(username=username).first()

        user.money += amount

        db.commit()
        db.refresh(user)

        return user

def add_friend(friend_username: str, my_id: int):

    with get_db() as db:
        friend = db.query(User).filter_by(username=friend_username).first()

        if not friend:
            return None

        current_user = db.query(User).filter_by(id=my_id).first()

        current_user.friends.append(friend)

        db.add(current_user)
        db.commit()
        db.refresh(current_user)

        return current_user