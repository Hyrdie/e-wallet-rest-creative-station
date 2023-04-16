import sqlalchemy as sa
from orm.db import users, users_token

def get_user_login(session, username):
    sql = sa.select(users).where(users.c.email == username)
    result = session.execute(sql)
    return result

def get_user_by_username(session, username):
    sql = sa.select(users).where(users.c.username == username)
    result = session.execute(sql)
    return result

def get_user_by_id(session, id):
    sql = sa.select(users).where(users.c.id == id)
    result = session.execute(sql)
    return result

def get_user_token(session, user_id):
    sql = sa.select(users_token).where(users_token.c.id_user == user_id)
    result = session.execute(sql)
    return result

def update_user_token(session, access_token, user_id):
    sql = sa.update(users_token).where(users_token.c.id_user==user_id).values(access_token=access_token)
    result = session.execute(sql)
    return result

def initial_user_token(session, id_user, access_token):
    sql = sa.insert(users_token).values(id_user=id_user, access_token=access_token)
    result = session.execute(sql)
    return result

def add_user(session, username, password, email):
    sql = sa.insert(users).values(username=username, password=password, email=email)
    result = session.execute(sql)
    return result