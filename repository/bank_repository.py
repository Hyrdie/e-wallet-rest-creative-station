import sqlalchemy as sa
from orm.db import users_balance

def insert_user_balance(session, id_user, balance):
    sql = sa.insert(users_balance).values(id_user=id_user, balance=balance)
    result = session.execute(sql)
    return result

def get_user_balance(session, id_user):
    sql = sa.select(users_balance).where(users_balance.c.id_user == id_user)
    result = session.execute(sql)
    return result

def update_user_balance(session, id_user, balance):
    sql = sa.update(users_balance).where(users_balance.c.id_user == id_user).values(balance=balance)
    result = session.execute(sql)
    return result