
from fastapi import APIRouter, Depends

from services.auth import get_current_user
from services.card import create_card

router = APIRouter()


@router.post("/add-card")
def adding_card(is_credit: bool, user = Depends(get_current_user)):

    new_card = create_card(user.id, is_credit)

    return new_card
