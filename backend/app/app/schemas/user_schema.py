from app.utils.partial import optional
from app.models.user_model import UserBase
from app.models.group_model import GroupBase
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from enum import Enum
from .media_schema import IImageMediaRead
from .role_schema import IRoleRead


class IUserCreate(UserBase):
    password: Optional[str]

    class Config:
        hashed_password = None


# All these fields are optional
@optional
class IUserUpdate(UserBase):
    pass


# This schema is used to avoid circular import
class IGroupReadBasic(GroupBase):
    id: UUID


class IUserRead(UserBase):
    id: UUID
    role: Optional[IRoleRead] = None
    groups: Optional[List[IGroupReadBasic]] = []
    image: Optional[IImageMediaRead]
    follower_count: Optional[int] = 0
    following_count: Optional[int] = 0


class IUserReadWithoutGroups(UserBase):
    id: UUID
    role: Optional[IRoleRead] = None
    image: Optional[IImageMediaRead]
    follower_count: Optional[int] = 0
    following_count: Optional[int] = 0


class IUserBasicInfo(BaseModel):
    id: UUID
    first_name: str
    last_name: str


class IUserStatus(str, Enum):
    active = "active"
    inactive = "inactive"
