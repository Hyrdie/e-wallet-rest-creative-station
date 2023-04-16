from sqlalchemy import (Column, Integer, String, Table, Boolean, Numeric, Date, DateTime, Text)
from datetime import datetime

from orm.db_setup import metadata

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(100), unique=True, nullable=False ),
    Column('password', String(100), nullable=False),
    Column('email', String(100), nullable=False)
)

users_token = Table(
    'users_token',
    metadata,
    Column('id_user', Integer, primary_key=True),
    Column('access_token', String, nullable=False)
)

users_balance = Table(
    'users_balance',
    metadata,
    Column('id_user', Integer, primary_key=True),
    Column('balance', Integer, nullable=False)
)

transaction_log = Table(
    'transaction_log',
    metadata,
    Column('id_user', Integer, nullable=False),
    Column('transaction', String, nullable=False),
    Column('amount', Integer, nullable=False)
)

