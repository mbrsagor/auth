from datetime import datetime

from typing import Optional
from pydantic import BaseModel, EmailStr


class CreteUser(BaseModel):
    fullname: str
    username: str
    email: EmailStr
    password: str


class UserSignIn(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class UserList(BaseModel):
    id: int
    email: str
    created_at: datetime


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_model = True
