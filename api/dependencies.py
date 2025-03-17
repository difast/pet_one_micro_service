from sqlalchemy.orm import Session
from .db import get_db

def get_db_session():
    return next(get_db())