# CRUD functions for the Specialty model
from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.specialty import Specialty

from schemas.specialty import SpecialtyResponse

def fn_get_specialties(db: Session) -> list[SpecialtyResponse]:
    try:
        specialties = db.query(Specialty).all()
        return specialties
    except Exception as e:
        raise e

def fn_get_specialty(db: Session, specialty_id: int) -> SpecialtyResponse:
    try:
        specialty = db.query(Specialty).filter(Specialty.id == specialty_id).first()
        
        if not specialty:
            raise HTTPException(status_code=404, detail='Specialty not found')
        return specialty
    except Exception as e:
        raise e