
from fastapi import APIRouter, Depends, HTTPException, status

from schemas.card import CardOut
from services.auth import get_current_user
from services.card import create_card, delete_card

router = APIRouter()


@router.post("/add-card", response_model=CardOut, status_code=status.HTTP_201_CREATED)
def adding_card(is_credit: bool, user = Depends(get_current_user)):

    new_card = create_card(user.id, is_credit)

    return new_card


@router.delete("/remove-card", response_model=CardOut, status_code=status.HTTP_200_OK)
def remove_card(card_id):

    card_to_delete = delete_card(card_id)

    if not card_to_delete:
        raise HTTPException(status_code=404, detail="Card does not exist!")

    return card_to_delete

