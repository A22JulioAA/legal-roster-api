from fastapi import APIRouter

from schemas.offer import OfferResponse

offers_router = APIRouter(
    prefix='/offers',
    tags=['Offers'],
)

@offers_router.get(
    '/',
    summary='Get Offers',
    description='Get all offers',
    response_description='List of offers',
    response_model=list[OfferResponse],
    responses={
        200: {
            'description': 'List of offers',
            'model': list[OfferResponse],
        },
        500: {
            'description': 'Internal Server Error',
        },
    },
)
def get_offers() -> list[OfferResponse]:
    """
    Get all offers

    Returns:
        list[OfferResponse]
    """
    return [
        {
            'title': 'Offer 1',
            'description': 'Description 1',
            'is_active': True,
            'is_locked': False,
            'created_at': '2021-01-01T00:00:00',
            'updated_at': '2021-01-01T00:00:00',
        },
        {
            'title': 'Offer 2',
            'description': 'Description 2',
            'is_active': True,
            'is_locked': False,
            'created_at': '2021-01-01T00:00:00',
            'updated_at': '2021-01-01T00:00:00',
        },
    ]

@offers_router.get(
    '/{offer_id}',
    summary='Get Offer',
    description='Get an offer by ID',
    response_description='Offer',
    response_model=OfferResponse,
    responses={
        200: {
            'description': 'Offer',
            'model': OfferResponse,
        },
        404: {
            'description': 'Offer not found',
        },
        500: {
            'description': 'Internal Server Error',
        },
    },
)
def get_offer(offer_id: int) -> OfferResponse:
    return {
        'id': offer_id,
        'title': 'Offer 1',
        'description': 'Description 1',
        'is_active': True,
        'is_locked': False,
        'created_at': '2021-01-01T00:00:00',
        'updated_at': '2021-01-01T00:00:00',
    }

@offers_router.get(
    '/{profesional_id}/offers',
    summary='Get Offers by profesional',
    description='Get all offers by profesional',
    response_description='List of offers',
    response_model=list[OfferResponse],
    responses={
        200: {
            'description': 'List of offers',
            'model': list[OfferResponse],
        },
        404: {
            'description': 'Profesional not found',
        },
        500: {
            'description': 'Internal Server Error',
        },
    },
)
def get_offers_by_profesional(profesional_id: int) -> list[OfferResponse]:
    return [
        {
            'id': 1,
            'title': 'Offer 1',
            'description': 'Description 1',
            'professional_id': profesional_id,
            'is_active': True,
            'is_locked': False,
            'created_at': '2021-01-01T00:00:00',
            'updated_at': '2021-01-01T00:00:00',
        },
        {
            'id': 2,
            'title': 'Offer 2',
            'description': 'Description 2',
            'professional_id': profesional_id,
            'is_active': True,
            'is_locked': False,
            'created_at': '2021-01-01T00:00:00',
            'updated_at': '2021-01-01T00:00:00',
        },
    ]

@offers_router.get(
    '/{profesional_id}/offers/{offer_id}',
    summary='Get Offer by profesional',
    description='Get an offer by profesional ID',
    response_description='Offer',   
    response_model=OfferResponse,
    responses={
        200: {
            'description': 'Offer',
            'model': OfferResponse,
        },
        404: {
            'description': 'Profesional or offer not found',
        },
        500: {
            'description': 'Internal Server Error',
        },
    }
)
def get_offer_by_profesional(id_profesional: int, id_offer: int) -> OfferResponse:
    return {
        'id': id_offer,
        'title': 'Offer 1',
        'description': 'Description 1',
        'professional_id': id_profesional,
        'is_active': True,
        'is_locked': False,
        'created_at': '2021-01-01T00:00:00',
        'updated_at': '2021-01-01T00:00:00',
    }

@offers_router.get(
    '/specialty/{specialty_id}/offers',
    summary='Get Offers by specialty',
    description='Get all offers by specialty',
    response_description='List of offers',
    response_model=list[OfferResponse],
    responses={
        200: {
            'description': 'List of offers',
            'model': list[OfferResponse],
        },
        404: {
            'description': 'Specialty not found',
        },
        500: {
            'description': 'Internal Server Error',
        },
    },
)
def get_offers_by_specialty(specialty_id: int) -> list[OfferResponse]:
    return [
        {
            'id': 1,
            'title': 'Offer 1',
            'description': 'Description 1',
            'specialty_id': specialty_id,
            'is_active': True,
            'is_locked': False,
            'created_at': '2021-01-01T00:00:00',
            'updated_at': '2021-01-01T00:00:00',
        },
        {
            'id': 2,
            'title': 'Offer 2',
            'description': 'Description 2',
            'specialty_id': specialty_id,
            'is_active': True,
            'is_locked': False,
            'created_at': '2021-01-01T00:00:00',
            'updated_at': '2021-01-01T00:00:00',
        },
    ]