from datetime import timedelta
from os import getenv

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from auth.helpers import (
    authenticate_user,
    create_access_token,
    credential_exception,
    get_current_user,
    get_user_by_username,
    hash_password,
)
from auth.models import Token, User, UserCreate, UserOut
from main_api.db import get_db

access_token_expires = timedelta(minutes=int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register", response_model=UserOut)
def register(data: UserCreate, db: Session = Depends(get_db)):
    print("DEBUG payload:", data.model_dump())
    username = data.username.strip()
    if get_user_by_username(db, username):
        raise HTTPException(409, detail="Username already registered")
    try:
        hashed = hash_password(data.password)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    new_user = User(username=username, hashed_password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise credential_exception
    access_token = create_access_token(
        sub=user.username,
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token)

@router.get("/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
