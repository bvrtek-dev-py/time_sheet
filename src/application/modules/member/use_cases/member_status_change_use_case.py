from time_sheet.src.application.modules.member.use_cases.member_get_by_id_use_case import (
    MemberGetByIdUseCase,
)
from time_sheet.src.core.modules.member.dto.member import MemberDTO
from time_sheet.src.core.modules.member.enum.member_status import MemberStatus
from time_sheet.src.core.modules.member.repositories.member_repository import (
    IMemberRepository,
)


class MemberStatusChangeUseCase:
    def __init__(
        self, repository: IMemberRepository, get_by_id_use_case: MemberGetByIdUseCase
    ):
        self._repository = repository
        self._get_by_id_use_case = get_by_id_use_case

    async def execute(self, member_id: str, status: MemberStatus) -> MemberDTO:
        member_dto = await self._get_by_id_use_case.execute(member_id)
        member_dto.status = status.value

        return await self._repository.update(member_dto)
