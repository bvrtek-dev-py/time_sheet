from pydantic import BaseModel

from time_sheet.src.core.modules.member.enum.member_status import MemberStatus


class MemberBaseRequest(BaseModel):
    status: MemberStatus


class MemberUpdateRequest(MemberBaseRequest):
    pass
