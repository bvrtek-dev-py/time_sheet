from time_sheet.src.application.modules.member.use_cases.member_get_by_id_use_case import (
    MemberGetByIdUseCase,
)

from time_sheet.src.core.modules.member.repositories.member_repository import (
    IMemberRepository,
)


class MemberDeleteUseCase:
    def __init__(
        self, repository: IMemberRepository, get_by_id_use_case: MemberGetByIdUseCase
    ):
        self._repository = repository
        self._get_by_id_use_case = get_by_id_use_case

    async def execute(self, member_id: str) -> None:
        await self._get_by_id_use_case.execute(member_id)

        return await self._repository.delete(member_id=member_id)
