from sqlalchemy.orm import Session
from orm.db_setup import engine
from pydantic import ValidationError
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from .base import AuthenticatedBaseApi
from fastapi import Request
from repository.payment_repository import insert_transaction_log, take_balance
from repository.user_repository import get_user_by_username
from repository.bank_repository import get_user_balance

payment_api = InferringRouter()

@cbv(payment_api)
class Payment(AuthenticatedBaseApi):
    @payment_api.get('/balance/')
    async def get_balance(self, request:Request):
        try:
            body = await request.json()
            username = body.get('username')
            with Session(engine) as session:
                user = get_user_by_username(session, username).fetchone()
                user_balance = get_user_balance(session, user.id).fetchone()
                if not user_balance:
                    return self.make_response(message="failed", payload={'detail':'you can top up first'}, code=402)
                return self.make_response(message="success", payload={
                    'user_id': user.id,
                    'username': username,
                    'balance': user_balance.balance
                }, code=200)
        except ValidationError as e:
            return e.json()

    @payment_api.post('/payment-transaction/')
    async def payment_transaction(self, request:Request):
        try:
            body = await request.json()
            username, transaction, amount = body.get('username'), body.get('transaction'), body.get('amount')
            with Session(engine) as session:
                user = get_user_by_username(session, username).fetchone()
                user_balance = get_user_balance(session, user.id).fetchone()
                if not user_balance or user_balance.balance < amount:
                    return self.make_response(message="failed", payload={'detail':'insuficcient funds'}, code=402)

                final_balance = user_balance.balance-amount
                insert_transaction_log(session, user.id, transaction, amount)
                take_balance(session, user.id, final_balance)
                session.commit()
            return self.make_response(message="success", payload={'detail':{'transaction':transaction, 'amount':amount}}, code=200)
            # return self.make_response(message="success", payload={'detail':'test'}, code=200)
        except ValidationError as e:
            return e.json()