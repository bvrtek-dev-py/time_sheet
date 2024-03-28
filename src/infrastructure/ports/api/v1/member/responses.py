from pydantic import BaseModel

from time_sheet.src.core.modules.member.enum.member_status import MemberStatus
from time_sheet.src.infrastructure.ports.api.v1.project.responses import (
    ProjectBaseResponse,
)
from time_sheet.src.infrastructure.ports.api.v1.user.responses import UserBaseResponse


class MemberBaseResponse(BaseModel):
    id: str
    user: UserBaseResponse
    project: ProjectBaseResponse
    status: MemberStatus
