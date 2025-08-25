from fastapi import APIRouter
from fastapi.params import Depends

from services.auth import get_current_user
from services.transaction import send_money_to_user

router = APIRouter()


@router.post("/send-money")
def send_money(receiver_name: str, amount: float, current_user = Depends(get_current_user)):
    transaction = send_money_to_user(current_user.username, receiver_name, amount)

    return transaction
