from time_sheet.src.application.modules.member.dto.member import (
    MemberWithUserAndProjectDTO,
)
from time_sheet.src.core.modules.member.dto.member import MemberDTO


class MemberDTOToWithUserAndProjectMapper:
    def map(self, dto: MemberDTO) -> MemberWithUserAndProjectDTO:
        return MemberWithUserAndProjectDTO(**dto.model_dump())
