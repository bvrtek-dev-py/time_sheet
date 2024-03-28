from typing import List

from time_sheet.src.core.modules.member.dto.member import MemberDTO
from time_sheet.src.core.modules.member.enum.member_status import MemberStatus
from time_sheet.src.core.modules.member.repositories.member_repository import (
    IMemberRepository,
)


class MemberGetAllForProjectUseCase:
    def __init__(self, repository: IMemberRepository):
        self._repository = repository

    async def execute(
        self, project_id: str, status: MemberStatus | None = None
    ) -> List[MemberDTO]:
        return await self._repository.get_all_for_project(project_id, status)
