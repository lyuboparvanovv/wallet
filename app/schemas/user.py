from datetime import datetime

from pydantic import BaseModel, constr, EmailStr, field_validator, confloat
from typing import Optional, List

from schemas.card import CardOut


class UserBase(BaseModel):
    username: constr(min_length=2, max_length=20)
    password: str
    phone_number: constr(min_length=10, max_length=10)
    email: EmailStr
    is_admin: Optional[bool] = False

class UserBaseWithMoney(UserBase):
    money: confloat(ge=0.0)

class CreateUser(UserBase):
    password: constr(min_length=8)

    @field_validator('password')
    def password_complexity(cls, v):
        import re
        if not (re.search(r'[A-Z]', v) and re.search(r'\d', v) and re.search(r'[\+\-\*\&\^]', v)):
            raise ValueError(
                'Password must contain an uppercase letter, a digit, and a special character (+, -, *, &, ^)')
        return v

class UpdateUser(BaseModel):
    password: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None

class FriendsOut(BaseModel):
    username: str

    class Config:
        from_attributes = True

class TransactionOut(BaseModel):
    sender: str
    receiver: str
    amount: float
    date: datetime

    class Config:
        from_attributes = True

class UserWholeInfo(UserBaseWithMoney):
    cards: List[CardOut] = List
    friends: List[FriendsOut] = List
    transactions: List[TransactionOut] = List

    class Config:
        from_attributes = True
