from pydantic import BaseModel

from time_sheet.src.application.modules.project.dto.project import ProjectGetDTO
from time_sheet.src.application.modules.user.dto.user import UserGetDTO
from time_sheet.src.core.modules.member.enum.member_status import MemberStatus


class MemberBaseDTO(BaseModel):
    status: MemberStatus


class MemberCreateDTO(BaseModel):
    user_id: str
    project_id: str


class MemberWithUserAndProjectDTO(MemberBaseDTO):
    id: str
    user: UserGetDTO | None = None
    project: ProjectGetDTO | None = None
