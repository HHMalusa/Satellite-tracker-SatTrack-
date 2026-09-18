from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Satellite(Base):
    __tablename__ = "satellites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    norad_id = Column(Integer, unique=True, index=True)
