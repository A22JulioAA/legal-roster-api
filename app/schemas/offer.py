# FIXME: Check the name of the schema and model. offer could be conflictive in the future

from pydantic import BaseModel

from datetime import datetime

class OfferBase(BaseModel):
    title: str
    description: str
    is_active: bool
    is_locked: bool
    created_at: datetime
    updated_at: datetime

class OfferCreate(OfferBase):
    pass

class OfferUpdate(OfferBase):
    pass

class OfferInDB(OfferBase):
    pass

class OfferResponse(OfferBase):
    id: int
    professional_id: int
