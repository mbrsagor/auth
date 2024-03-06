from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text


class User(Base):
    """
    User Model
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    fullname = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    def __repr__(self):
        return self.fullname
