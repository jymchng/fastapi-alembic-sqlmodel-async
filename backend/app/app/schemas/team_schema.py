from app.models.hero_model import HeroBase
from app.models.team_model import TeamBase
from .user_schema import IUserBasicInfo
from app.utils.partial import optional
from typing import List, Optional
from uuid import UUID


class ITeamCreate(TeamBase):
    pass


# All these fields are optional
@optional
class ITeamUpdate(TeamBase):
    pass


class ITeamRead(TeamBase):
    id: UUID
    created_by: Optional[IUserBasicInfo] = None


class ITeamReadWithHeroes(ITeamRead):
    heroes: List[HeroBase]
