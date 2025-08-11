from pydantic import BaseModel, Field, SecretStr
from typing import Optional
from  datetime import datetime
from uuid import UUID


# Это база
class UserBase(BaseModel):
    username: str = Field(..., max_length=70)
    account_name: str  =  Field(..., max_length=70)


# Для POST
class UserCreate(UserBase):
    password: SecretStr = Field(..., min_length=8, max_length=70)


# Для PATCH
class UserUpdate(UserBase):
    account_name: Optional[str] = Field(None, min_length=1, max_length=128)
    password: Optional[SecretStr] = Field(None, min_length=8, max_length=70)


# Для API
class UserResponse(UserBase):
    id: UUID
    date_joined: datetime

    class Config:
        from_attributes = True
