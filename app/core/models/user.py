from app.core.models.database import Base
from sqlalchemy import Column, Integer, String, Float

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    balance = Column(Float, default=0.0)