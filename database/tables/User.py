from sqlalchemy import Column, Integer, BigInteger, DateTime, String

from database.db_session import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)

    chat_id = Column(BigInteger, unique=True)
    username = Column(String)
    first_name = Column(String)

    created_at = Column(DateTime)