from time_sheet.src.application.modules.member.dto.member import MemberCreateDTO
from time_sheet.src.core.modules.member.dto.member import MemberDTO
from time_sheet.src.core.modules.member.enum.member_status import MemberStatus
from time_sheet.src.core.modules.member.repositories.member_repository import (
    IMemberRepository,
)


class MemberSendRequestUseCase:
    def __init__(self, repository: IMemberRepository):
        self._repository = repository

    async def execute(self, request_dto: MemberCreateDTO) -> MemberDTO:
        member_dto = MemberDTO(
            **request_dto.model_dump() | {"status": MemberStatus.WAITING_MEMBER},
            _id=None,
        )

        return await self._repository.save(member_dto)
