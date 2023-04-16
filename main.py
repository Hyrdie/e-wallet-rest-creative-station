import uvicorn
from fastapi import FastAPI
from settings import settings
from fastapi.middleware.cors import CORSMiddleware
from orm import db
from orm.db_setup import metadata, database, engine
import logging
from utils.hashing import Hasher
from api.login_api import login_router
from api.users_api import users_api
from api.bank_api import bank_api
from api.payment_api import payment_api

app = FastAPI(title=settings.APP_NAME)

db.metadata.create_all(engine)
logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

origins = settings.ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS
)

@app.get("/alive")
async def getInfo():
    return {
        "desc":"Microservices for e-wallet"
    }

@app.on_event("startup")
async def startup():
    await database.connect()
    user = await database.fetch_all(query="SELECT * FROM users")
    if len(user) == 0:
        logging.info('User not found. Creating...')
        email = "admin@gmail.com"
        password = Hasher.get_password_hash("admin")
        sqls = [
            f"insert into users (username, password, email) values ('adiva','{password}','{email}')"
        ]
        for sql in sqls:
            await database.execute(query=sql)
    logger.info("e-wallet service is up!!!")

@app.on_event("shutdown")
async def shutdown():
    logger.info("shutting down e-wallet service...")

app.include_router(users_api, tags=["sign up"])
app.include_router(login_router, tags=["sign in"])
app.include_router(payment_api, tags=["payment"])
app.include_router(bank_api, tags=["bank third party / topup"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)