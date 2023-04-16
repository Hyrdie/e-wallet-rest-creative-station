from typing import Any, Dict
from fastapi_utils.cbv import cbv
from fastapi import APIRouter, Header, Response, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import MetaData, create_engine
from jose import jwt,JWTError
from fastapi.exceptions import HTTPException

from orm.db_setup import get_db
from settings import settings
from repository.user_repository import get_user_by_id

from api.tools import OAuth2PasswordBearerWithCookie

oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/login/token")

class BaseApi():
    db: Session = Depends(get_db)
    engine = create_engine(settings.DATABASE_URL)

    def make_response(self, payload: dict = {}, message: str = 'success', meta: dict = {}, code: int = 200):
        return JSONResponse(status_code=code, content={"message": message, "meta":meta, "data": payload})


class UnauthenticatedBaseApi(BaseApi):
    """
    Base class for unauthenticated route api
    """
    def __init__(self):
        super(UnauthenticatedBaseApi, self).__init__()


class AuthenticatedBaseApi(BaseApi):
    """
    Base class for authenticated route api
    """
    token: str = Depends(oauth2_scheme)

    def __init__(self):
        super(AuthenticatedBaseApi, self).__init__()

    @property
    def user(self):
        """
        property for getting current logged in user
        """
        credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                              detail="Could not validate credentials")
        try:
            payload: Dict = jwt.decode(self.token, settings.SECRET_KEY, algorithms=['HS256'])
        except JWTError:
            raise credentials_exception
        user = get_user_by_id(id=payload['id'], db=self.db)
        if user is None:
            raise credentials_exception
        return user