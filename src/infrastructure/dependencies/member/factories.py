# pylint: disable=R0913,C0301
from typing import Annotated

from fastapi import Depends
from motor.core import AgnosticClientSession

from time_sheet.src.adapters.modules.member.repositories.member_repository import (
    MemberRepository,
)
from time_sheet.src.application.modules.member.mapper.member_dto_to_with_user_and_project_mapper import (
    MemberDTOToWithUserAndProjectMapper,
)
from time_sheet.src.application.modules.member.services.member_service import (
    MemberService,
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
from time_sheet.src.core.modules.member.repositories.member_repository import (
    IMemberRepository,
)
from time_sheet.src.infrastructure.dependencies.database.setup import get_session
from time_sheet.src.infrastructure.dependencies.project.factories import (
    get_project_dto_to_get_mapper,
    get_project_get_by_id_use_case,
    get_project_load_owner_use_case,
)
from time_sheet.src.infrastructure.dependencies.user.factories import (
    get_user_dto_to_get_mapper,
    get_user_get_by_id_use_case,
)


def get_member_dto_to_with_user_and_project_mapper() -> (
    MemberDTOToWithUserAndProjectMapper
):
    return MemberDTOToWithUserAndProjectMapper()


def get_member_repository(
    session: Annotated[AgnosticClientSession, Depends(get_session)]
) -> IMemberRepository:
    return MemberRepository(session)


def get_member_send_request_use_case(
    repository: Annotated[IMemberRepository, Depends(get_member_repository)]
) -> MemberSendRequestUseCase:
    return MemberSendRequestUseCase(repository)


def get_member_get_by_id_use_case(
    repository: Annotated[IMemberRepository, Depends(get_member_repository)]
) -> MemberGetByIdUseCase:
    return MemberGetByIdUseCase(repository)


def get_member_get_all_for_project_use_case(
    repository: Annotated[IMemberRepository, Depends(get_member_repository)]
) -> MemberGetAllForProjectUseCase:
    return MemberGetAllForProjectUseCase(repository)


def get_member_get_by_user_id_use_case(
    repository: Annotated[IMemberRepository, Depends(get_member_repository)]
) -> MemberGetByUserIdUseCase:
    return MemberGetByUserIdUseCase(repository)


def get_member_status_change_use_case(
    repository: Annotated[IMemberRepository, Depends(get_member_repository)],
    get_by_id_use_case: Annotated[
        MemberGetByIdUseCase, Depends(get_member_get_by_id_use_case)
    ],
) -> MemberStatusChangeUseCase:
    return MemberStatusChangeUseCase(
        repository=repository, get_by_id_use_case=get_by_id_use_case
    )


def get_member_delete_use_case(
    repository: Annotated[IMemberRepository, Depends(get_member_repository)],
    get_by_id_use_case: Annotated[
        MemberGetByIdUseCase, Depends(get_member_get_by_id_use_case)
    ],
) -> MemberDeleteUseCase:
    return MemberDeleteUseCase(
        repository=repository, get_by_id_use_case=get_by_id_use_case
    )


def get_member_load_user_and_project_use_case(
    member_dto_to_with_user_and_project_mapper: Annotated[
        MemberDTOToWithUserAndProjectMapper,
        Depends(get_member_dto_to_with_user_and_project_mapper),
    ],
    user_dto_to_get_mapper: Annotated[
        UserDTOToGetMapper, Depends(get_user_dto_to_get_mapper)
    ],
    project_dto_to_get_mapper: Annotated[
        ProjectDTOToGetMapper, Depends(get_project_dto_to_get_mapper)
    ],
    user_get_by_id_use_case: Annotated[
        UserGetByIdUseCase, Depends(get_user_get_by_id_use_case)
    ],
    project_get_by_id_use_case: Annotated[
        ProjectGetByIdUseCase, Depends(get_project_get_by_id_use_case)
    ],
    project_load_owner_use_case: Annotated[
        ProjectLoadOwnerUseCase, Depends(get_project_load_owner_use_case)
    ],
) -> MemberLoadUserAndProjectUseCase:
    return MemberLoadUserAndProjectUseCase(
        member_dto_to_with_user_and_project_mapper=member_dto_to_with_user_and_project_mapper,
        user_get_by_id_use_case=user_get_by_id_use_case,
        user_dto_to_get_mapper=user_dto_to_get_mapper,
        project_get_by_id_use_case=project_get_by_id_use_case,
        project_dto_to_get_mapper=project_dto_to_get_mapper,
        project_load_owner_use_case=project_load_owner_use_case,
    )


def get_member_service(
    member_send_request_use_case: Annotated[
        MemberSendRequestUseCase, Depends(get_member_send_request_use_case)
    ],
    member_status_change_use_case: Annotated[
        MemberStatusChangeUseCase, Depends(get_member_status_change_use_case)
    ],
    member_delete_use_case: Annotated[
        MemberDeleteUseCase, Depends(get_member_delete_use_case)
    ],
    member_get_by_id_use_case: Annotated[
        MemberGetByIdUseCase, Depends(get_member_get_by_id_use_case)
    ],
    member_get_all_for_project_use_case: Annotated[
        MemberGetAllForProjectUseCase, Depends(get_member_get_all_for_project_use_case)
    ],
    member_get_by_user_id_use_case: Annotated[
        MemberGetByUserIdUseCase, Depends(get_member_get_by_user_id_use_case)
    ],
    load_user_and_project_use_case: Annotated[  # pylint: disable=C0301
        MemberLoadUserAndProjectUseCase,
        Depends(get_member_load_user_and_project_use_case),
    ],
) -> MemberService:
    return MemberService(
        member_send_request_use_case=member_send_request_use_case,
        member_status_change_use_case=member_status_change_use_case,
        delete_use_case=member_delete_use_case,
        get_all_for_project_use_case=member_get_all_for_project_use_case,
        get_by_id_use_case=member_get_by_id_use_case,
        get_by_user_id=member_get_by_user_id_use_case,
        load_user_and_project_use_case=load_user_and_project_use_case,
    )
