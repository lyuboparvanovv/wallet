from db.database import Base
from sqlalchemy import Column, Boolean, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    number = Column(String(16), unique=True, nullable=False)
    exp_date = Column(Date, nullable=False)
    cvv = Column(Integer, nullable=False)
    is_credit = Column(Boolean, default=False)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False,index=True)
    user = relationship("User", back_populates="cards")
