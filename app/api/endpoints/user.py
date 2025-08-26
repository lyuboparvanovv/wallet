from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status

from schemas.token import Token
from schemas.user import CreateUser, UpdateUser, UserWholeInfo, UserOut
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from services.auth import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_user
from services.user import create_user, update_user, add_money, add_friend, get_user_whole_info

router = APIRouter()

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register_user(new_user: CreateUser):
    user = create_user(new_user)

    if not user:
        raise HTTPException(status_code=409, detail="User already exist!")

    return user

@router.post("/token")
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@router.get("/me", response_model=UserWholeInfo, status_code=status.HTTP_200_OK)
def read_users_me(current_user = Depends(get_current_user)):

    user = get_user_whole_info(user_id=current_user.id)

    return user


@router.put("/update-profile", response_model=UserOut, status_code=status.HTTP_200_OK)
def update_profile(update_info: UpdateUser, current_user = Depends(get_current_user)):
    updated_user = update_user(username=current_user.username, updated_user=update_info)

    return updated_user


@router.put("/deposit", status_code=status.HTTP_200_OK)
def adding_money_to_card(amount: float,current_user =  Depends(get_current_user)):

    updated_user = add_money(current_user.username, amount)

    return updated_user

@router.post("/add-contact", response_model=UserOut, status_code=status.HTTP_200_OK)
def add_new_contact(contact_username: str, current_user = Depends(get_current_user)):

    new_contact = add_friend(contact_username, current_user.id)

    if not new_contact:

        raise HTTPException(status_code=404, detail="User not found!")

    return new_contact