from datetime import datetime

from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from db.database import Base


class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.now)

    sender = relationship(
        "User",
        foreign_keys=[sender_id],
        back_populates="sent_transactions"
    )
    receiver = relationship(
        "User",
        foreign_keys=[receiver_id],
        back_populates="received_transactions"
    )