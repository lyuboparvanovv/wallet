from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
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