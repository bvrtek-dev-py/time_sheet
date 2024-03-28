from typing import List

from time_sheet.src.core.modules.common.exceptions.domain import ObjectDoesNotExist
from time_sheet.src.core.modules.member.dto.member import MemberDTO
from time_sheet.src.core.modules.member.repositories.member_repository import (
    IMemberRepository,
)


class MemberGetByUserIdUseCase:
    def __init__(self, repository: IMemberRepository):
        self._repository = repository

    async def execute(self, user_id: str) -> List[MemberDTO]:
        members = await self._repository.get_by_user_id(user_id=user_id)

        if members is None:
            raise ObjectDoesNotExist

        return members
