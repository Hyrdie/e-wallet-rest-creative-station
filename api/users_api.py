from sqlalchemy.orm import Session
from orm.db_setup import engine
from pydantic import ValidationError
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from .base import UnauthenticatedBaseApi
from utils.hashing import Hasher
from fastapi import Request
from repository.user_repository import add_user

users_api = InferringRouter()

@cbv(users_api)
class Users(UnauthenticatedBaseApi):
    @users_api.post('/users/', status_code=201)
    async def add_users(self, request:Request):
        try:
            body = await request.json()
            username, raw_pass, email = body.get('username'), body.get('password'), body.get('email')
            password = Hasher.get_password_hash(raw_pass)
            with Session(engine) as session:
                add_user(session, username, password, email)
                session.commit()
            return self.make_response(message="success", payload={'username': username, 'pass': raw_pass}, code=201)
        except ValidationError as e:
            return e.json()