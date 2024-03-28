# pylint: disable=C0301,R0913
from time_sheet.src.application.modules.member.dto.member import (
    MemberWithUserAndProjectDTO,
)
from time_sheet.src.application.modules.member.mapper.member_dto_to_with_user_and_project_mapper import (
    MemberDTOToWithUserAndProjectMapper,
)
from time_sheet.src.application.modules.project.mapper.project_dto_to_get_mapper import (
    ProjectDTOToGetMapper,
)
from time_sheet.src.application.modules.project.use_cases.project_get_by_id_use_case import (
    ProjectGetByIdUseCase,
)
from time_sheet.src.application.modules.project.use_cases.project_load_owner_use_case import (
    ProjectLoadOwnerUseCase,
)
from time_sheet.src.application.modules.user.mapper.user_dto_to_get_mapper import (
    UserDTOToGetMapper,
)
from time_sheet.src.application.modules.user.use_cases.user_get_by_id_use_case import (
    UserGetByIdUseCase,
)
from time_sheet.src.core.modules.member.dto.member import MemberDTO


class MemberLoadUserAndProjectUseCase:
    def __init__(
        self,
        member_dto_to_with_user_and_project_mapper: MemberDTOToWithUserAndProjectMapper,
        user_dto_to_get_mapper: UserDTOToGetMapper,
        project_dto_to_get_mapper: ProjectDTOToGetMapper,
        user_get_by_id_use_case: UserGetByIdUseCase,
        project_get_by_id_use_case: ProjectGetByIdUseCase,
        project_load_owner_use_case: ProjectLoadOwnerUseCase,
    ):
        self._member_dto_to_with_user_and_project_mapper = (
            member_dto_to_with_user_and_project_mapper
        )
        self._user_dto_to_get_mapper = user_dto_to_get_mapper
        self._project_dto_to_get_mapper = project_dto_to_get_mapper
        self._user_get_by_id_use_case = user_get_by_id_use_case
        self._project_get_by_id_use_case = project_get_by_id_use_case
        self._project_load_owner_use_case = project_load_owner_use_case

    async def execute(self, member: MemberDTO) -> MemberWithUserAndProjectDTO:
        user_dto = await self._user_get_by_id_use_case.execute(member.user_id)

        project_dto = await self._project_get_by_id_use_case.execute(member.project_id)
        project_with_owner_dto = await self._project_load_owner_use_case.execute(
            project_dto
        )

        mapped_member = self._member_dto_to_with_user_and_project_mapper.map(member)
        mapped_member.user = self._user_dto_to_get_mapper.map(user_dto)
        mapped_member.project = self._project_dto_to_get_mapper.map(
            project_with_owner_dto
        )

        return mapped_member
