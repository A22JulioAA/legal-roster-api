from sqlalchemy import Column, Integer, String, func
from sqlalchemy.orm import relationship

from config.database import Base

class Specialty(Base):
    __tablename__ = 'specialties'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    description = Column(String, nullable=False)
    created_at = Column(String, default=func.now(), nullable=False)
    updated_at = Column(String, default=func.now(), onupdate=func.now(), nullable=False)

    