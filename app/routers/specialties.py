from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_db

from schemas.specialty import SpecialtyResponse, SpecialtyCreate

from CRUD.specialtyCRUD import fn_get_specialties, fn_get_specialty, fn_create_specialty

specialties_router = APIRouter(
    prefix='/specialties',
    tags=['Specialties'],
)

@specialties_router.get(
    '/',
    summary='Get Specialties',
    description='Get all specialties',
    response_description='List of specialties',
    response_model=list[SpecialtyResponse],
    responses={
        200: {
            'description': 'List of specialties',
            'model': list[SpecialtyResponse],
        },
        500: {
            'description': 'Internal Server Error',
        },
    },
)
def get_specialties(db: Session = Depends(get_db)) -> list[SpecialtyResponse]:
    """
    Get all specialties

    Returns:
        list[SpecialtyResponse]
    """
    specialties = fn_get_specialties(db)
    return specialties

@specialties_router.get(
    '/{specialty_id}',
    summary='Get Specialty',
    description='Get a specialty by ID',
    response_description='Specialty',
    response_model=SpecialtyResponse,
    responses={
        200: {
            'description': 'Specialty',
            'model': SpecialtyResponse,
        },
        404: {
            'description': 'Specialty not found',
        },
        500: {
            'description': 'Internal Server Error',
        },
    },
)   
def get_specialty(specialty_id: int, db: Session = Depends(get_db)) -> SpecialtyResponse:
    """
    Get a specialty by ID

    Args:
        specialty_id (int): Specialty ID

    Returns:
        SpecialtyResponse
    """
    specialty = fn_get_specialty(db, specialty_id)
    return specialty

@specialties_router.post(
    '/',
    summary='Create Specialty',
    description='Create a new specialty',
    response_description='Specialty',
    response_model=SpecialtyResponse,
    responses={
        201: {
            'description': 'Specialty created',
            'model': SpecialtyResponse,
        },
        422: {
            'description': 'Unprocessable Entity',
        },
        500: {
            'description': 'Internal Server Error',
        },
    },
)
def create_specialty(specialty: SpecialtyCreate, db: Session = Depends(get_db)) -> SpecialtyResponse:
    """
    Create a new specialty

    Returns:
        SpecialtyResponse
    """
    new_specialty = fn_create_specialty(db, specialty)
    return new_specialty