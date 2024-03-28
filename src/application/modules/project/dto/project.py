from pydantic import BaseModel

from time_sheet.src.application.modules.user.dto.user import UserGetDTO


class ProjectBaseDTO(BaseModel):
    name: str
    description: str


class ProjectCreateDTO(ProjectBaseDTO):
    owner_id: str


class ProjectUpdateDTO(ProjectBaseDTO):
    pass


class ProjectGetDTO(ProjectBaseDTO):
    id: str
    owner: UserGetDTO | None = None


class ProjectWithOwnerDTO(ProjectBaseDTO):
    id: str
    owner: UserGetDTO | None = None
