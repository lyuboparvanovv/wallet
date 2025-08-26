from fastapi import APIRouter, status
from fastapi.params import Depends

from schemas.user import TransactionOut
from services.auth import get_current_user
from services.transaction import send_money_to_user

router = APIRouter()


@router.post("/send-money", status_code=status.HTTP_201_CREATED)
def send_money(receiver_name: str, amount: float, current_user = Depends(get_current_user)):
    transaction = send_money_to_user(current_user.username, receiver_name, amount)

    return transaction
