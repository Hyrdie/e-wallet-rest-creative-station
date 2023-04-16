import sqlalchemy as sa
from orm.db import transaction_log, users_balance

def insert_transaction_log(session, id_user, transaction, amount):
    sql = sa.insert(transaction_log).values(id_user=id_user, transaction=transaction, amount=amount)
    result = session.execute(sql)
    return result

def take_balance(session, user_id, balance):
    sql = sa.update(users_balance).where(users_balance.c.id_user == user_id).values(balance=balance)
    result = session.execute(sql)
    return result