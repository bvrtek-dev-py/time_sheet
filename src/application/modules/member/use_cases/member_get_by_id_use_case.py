from time_sheet.src.core.modules.common.exceptions.domain import ObjectDoesNotExist
from time_sheet.src.core.modules.member.dto.member import MemberDTO
from time_sheet.src.core.modules.member.repositories.member_repository import (
    IMemberRepository,
)


class MemberGetByIdUseCase:
    def __init__(self, repository: IMemberRepository):
        self._repository = repository

    async def execute(self, member_id: str) -> MemberDTO:
        member = await self._repository.get_by_id(member_id=member_id)

        if member is None:
            raise ObjectDoesNotExist

        return member
