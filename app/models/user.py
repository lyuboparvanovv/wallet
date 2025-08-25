from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

from models.friends import friends_table
from models.transaction import Transaction


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False, unique=True)
    money = Column(Float, default=0)
    is_admin = Column(Boolean, default=False)

    cards = relationship("Card", back_populates="user", cascade="all, delete-orphan")
    friends = relationship("User", secondary="friends",
                           primaryjoin=id==friends_table.c.user_id,
                           secondaryjoin=id==friends_table.c.friend_id,
                           backref="friend_of")

    sent_transactions = relationship(
        "Transaction",
        foreign_keys=[Transaction.sender_id],
        back_populates="sender",
    )
    received_transactions = relationship(
        "Transaction",
        foreign_keys=[Transaction.receiver_id],
        back_populates="receiver",
    )

