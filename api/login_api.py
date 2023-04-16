from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Header, Response, Depends, status
from fastapi.exceptions import HTTPException
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from sqlalchemy import text as sa_text
from datetime import timedelta
from utils.security import create_access_token
from utils.hashing import Hasher
from repository.user_repository import get_user_login, get_user_token, update_user_token, initial_user_token
from orm.db_setup import engine

from .base import UnauthenticatedBaseApi

login_router = InferringRouter()

def authenticate_user(username:str, password:str):
    with Session(engine) as session:
        user = get_user_login(session, username=username)
        for data in user:        
            if not data:
                return False
            if not Hasher.verify_password(password, data.password):
                return False
            return data

@cbv(login_router)
class Login(UnauthenticatedBaseApi):
    
    @login_router.post("/login/token")
    def post_login(self, response: Response, form_data: OAuth2PasswordRequestForm=Depends()):
        user = authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password.")
        access_token_expire = timedelta(minutes=30)
        access_token = create_access_token(data={
            "id": user.id,
            "username": user.username,
            "email": user.email
        })
        response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
        with Session(engine) as session:
            check_user_token = get_user_token(session, user.id).fetchone()
            if not check_user_token:
                initial_user_token(session, user.id, access_token)
                session.commit()
                return self.make_response(message="success", payload={"access_token":access_token, "token_type":"Bearer"}, code=200)
            else:
                update_user_token(session, access_token, user.id)
                session.commit()
                return self.make_response(message="success", payload={"access_token":access_token,"token_type":"Bearer"}, code=200)