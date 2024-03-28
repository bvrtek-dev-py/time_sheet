# pylint: disable=R0801, R0913, C0301
from typing import List

from time_sheet.src.application.modules.member.dto.member import (
    MemberCreateDTO,
    MemberWithUserAndProjectDTO,
)
from time_sheet.src.application.modules.member.use_cases.member_send_request_use_case import (
    MemberSendRequestUseCase,
)
from time_sheet.src.application.modules.member.use_cases.member_delete_use_case import (
    MemberDeleteUseCase,
)
from time_sheet.src.application.modules.member.use_cases.member_get_all_for_project_use_case import (
    MemberGetAllForProjectUseCase,
)
from time_sheet.src.application.modules.member.use_cases.member_get_by_id_use_case import (
    MemberGetByIdUseCase,
)
from time_sheet.src.application.modules.member.use_cases.member_get_by_user_id_use_case import (
    MemberGetByUserIdUseCase,
)
from time_sheet.src.application.modules.member.use_cases.member_load_user_and_project_use_case import (
    MemberLoadUserAndProjectUseCase,
)
from time_sheet.src.application.modules.member.use_cases.member_status_change_use_case import (
    MemberStatusChangeUseCase,
)
from time_sheet.src.core.modules.member.enum.member_status import MemberStatus


class MemberService:
    def __init__(
        self,
        member_send_request_use_case: MemberSendRequestUseCase,
        delete_use_case: MemberDeleteUseCase,
        member_status_change_use_case: MemberStatusChangeUseCase,
        get_all_for_project_use_case: MemberGetAllForProjectUseCase,
        get_by_id_use_case: MemberGetByIdUseCase,
        get_by_user_id: MemberGetByUserIdUseCase,
        load_user_and_project_use_case: MemberLoadUserAndProjectUseCase,
    ):
        self._member_send_request_use_case = member_send_request_use_case
        self._delete_use_case = delete_use_case
        self._member_status_change_use_case = member_status_change_use_case
        self._get_all_for_project_use_case = get_all_for_project_use_case
        self._get_by_id_use_case = get_by_id_use_case
        self._get_by_user_id = get_by_user_id
        self._load_user_and_project_use_case = load_user_and_project_use_case

    async def create(self, request_dto: MemberCreateDTO) -> MemberWithUserAndProjectDTO:
        member = await self._member_send_request_use_case.execute(request_dto)

        return await self._load_user_and_project_use_case.execute(member)

    async def update(
        self, member_id: str, status: MemberStatus
    ) -> MemberWithUserAndProjectDTO:
        member = await self._member_status_change_use_case.execute(
            member_id=member_id, status=status
        )

        return await self._load_user_and_project_use_case.execute(member)

    async def delete(self, member_id: str) -> None:
        return await self._delete_use_case.execute(member_id)

    async def get_all_for_project(
        self, project_id, status: MemberStatus | None = None
    ) -> List[MemberWithUserAndProjectDTO]:
        members = await self._get_all_for_project_use_case.execute(project_id, status)

        return [
            await self._load_user_and_project_use_case.execute(member)
            for member in members
        ]

    async def get_by_id(self, member_id: str) -> MemberWithUserAndProjectDTO:
        member = await self._get_by_id_use_case.execute(member_id)

        return await self._load_user_and_project_use_case.execute(member)

    async def get_by_user_id(self, user_id: str) -> List[MemberWithUserAndProjectDTO]:
        members = await self._get_by_user_id.execute(user_id)

        return [
            await self._load_user_and_project_use_case.execute(member)
            for member in members
        ]

    async def get_participates(self, user_id: str) -> List[MemberWithUserAndProjectDTO]:
        members = await self._get_by_user_id.execute(user_id)

        return [
            await self._load_user_and_project_use_case.execute(member)
            for member in members
            if member.status == MemberStatus.MEMBER.value
        ]
