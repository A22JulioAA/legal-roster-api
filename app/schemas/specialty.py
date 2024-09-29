from pydantic import BaseModel
from datetime import datetime

class SpecialtyBase(BaseModel):
    name: str
    description: str

class SpecialtyCreate(SpecialtyBase):
    pass

class SpecialtyUpdate(SpecialtyBase):
    name: str | None
    description: str | None

class SpecialtyInDB(SpecialtyBase):
    id: int
    created_at: datetime
    updated_at: datetime

class SpecialtyResponse(SpecialtyBase):
    id: int