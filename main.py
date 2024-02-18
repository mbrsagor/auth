import models
from database import engine
from fastapi import FastAPI
from auth_router import signup_api, signin_api

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(signup_api.router, prefix="signup", tags=["signup"])
app.include_router(signin_api.router, prefix="signin", tags=["signin"])
