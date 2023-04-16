from sqlalchemy.orm import Session
from orm.db_setup import engine
from pydantic import ValidationError
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from .base import AuthenticatedBaseApi
from fastapi import Request
from repository.user_repository import get_user_by_username
from repository.bank_repository import insert_user_balance, get_user_balance, update_user_balance
import random

bank_api = InferringRouter()

@cbv(bank_api)
class Bank(AuthenticatedBaseApi):
    @bank_api.post('/topup/')
    async def add_balance(self, request:Request):
        try:
            body = await request.json()
            username, amount = body.get('username'), body.get('amount')
            with Session(engine) as session:
                user = get_user_by_username(session, username).fetchone()
                if not user:
                    return self.make_response(message="error", payload={'status':'FAILED', 'detail':'user does not exist'}, code=400)
                else:
                    if random.random() < 0.20:
                        return self.make_response(message="failed", payload={'status':'DECLINED', 'detail':'declined from bank'}, code=402)
                    else:
                        users_balance = get_user_balance(session, user.id).fetchone()
                        if not users_balance:
                            insert_user_balance(session, user.id, amount)
                            session.commit()
                            return self.make_response(message="success", payload={
                                'status':'SUCCESS'
                                }, code=200)
                        else:
                            balance = users_balance.balance
                            update_user_balance(session, user.id, amount+balance)
                            session.commit()
                            return self.make_response(message="success", payload={'status':'SUCCESS'}, code=200)
        except ValidationError as e:
            return e.json()