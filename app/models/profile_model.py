from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import Date
from app import db
from sqlalchemy import Column, Integer, String, Date


class Profile(db.Model):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)

    title = Column(String(50), nullable=False, unique=True)
    date = Column(Date, nullable=False)
    content = Column(String, nullable=False)
    writer = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
