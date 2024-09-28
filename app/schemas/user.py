from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    is_superuser: bool
    is_locked: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str

class UserResponse(UserBase):
    pass
