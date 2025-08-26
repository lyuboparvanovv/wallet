from db.database import get_db
from models.transaction import Transaction
from models.user import User
from fastapi import HTTPException


def send_money_to_user(sender_name, receiver_name, amount):

    with get_db() as db:

        sender = db.query(User).filter_by(username=sender_name).first()

        receiver = db.query(User).filter_by(username=receiver_name).first()

        if not receiver:
            raise HTTPException(status_code=404, detail="Receiver not found!")

        if sender.money < amount:
            raise HTTPException(status_code=400, detail="Not enough money.")

        sender.money -= amount
        receiver.money += amount

        transaction = Transaction(
            sender_id = sender.id,
            receiver_id = receiver.id,
            amount = amount,
        )
        db.add(transaction)
        db.commit()
        db.refresh(transaction)

        return transaction