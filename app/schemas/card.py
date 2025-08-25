from datetime import date
from typing import Optional
from pydantic import BaseModel, constr

class CreateCard(BaseModel):

    number: constr(pattern=r'^\d{16}$')
    exp_date: date
    cvv: constr(pattern=r'^\d{3}$')
    is_credit: Optional[bool] = False

class CardOut(BaseModel):

    id: int
    number: str
    exp_date: date
    is_credit: bool

    class Config:
        from_attributes = True
