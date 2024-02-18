from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from oauth2 import create_access_token
from utils import varify_password, hash_password
from database import get_db
from schemas import CreteUser, UserOut
from models import User

router = APIRouter(
    tags=['Auth']
)


@router.post('/signup/', status_code=status.HTTP_201_CREATED, response_model=UserOut)
def signup_api(user: CreteUser, db: Session = Depends(get_db)):
    """
    Create new user with Has password
    :param user:
    :param db:
    :return:
    """
    # Has the password - user.password
    hashed_password = hash_password(user.password)
    user.password = hashed_password

    new_user = User(**user.dict())

    # Check if a user with the same email already exists
    db_user = db.query(User).filter(User.email == new_user.email).first()
    if db_user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with the email already exists.')

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post('/signin/')
async def signin_api(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    User signIN with access token and validate credentials
    :param user_credentials:
    :param db:
    :return:
    """
    user = db.query(User).filter(User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials.")
    if not varify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect password.')

    access_token = create_access_token(data={'user_id': user.id, 'email': user.email})
    return {"access_token": access_token, "token_type": "bearer"}
