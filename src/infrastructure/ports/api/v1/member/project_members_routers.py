from typing import Annotated, List

from fastapi import APIRouter, Depends, status

from time_sheet.src.application.modules.member.dto.member import MemberCreateDTO
from time_sheet.src.application.modules.member.services.member_service import (
    MemberService,
)
from time_sheet.src.core.modules.auth.dto.auth import CurrentUserDTO
from time_sheet.src.core.modules.member.enum.member_status import MemberStatus
from time_sheet.src.infrastructure.dependencies.auth.permissions import get_current_user
from time_sheet.src.infrastructure.dependencies.member.factories import (
    get_member_service,
)
from time_sheet.src.infrastructure.ports.api.v1.common.responses import ErrorResponse
from time_sheet.src.infrastructure.ports.api.v1.member.responses import (
    MemberBaseResponse,
)

router = APIRouter(prefix="/api/v1/projects", tags=["APIv1 Project"])


@router.post(
    "/{project_id}/members",
    response_model=MemberBaseResponse,
    responses={
        201: {"model": MemberBaseResponse},
        404: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
    },
    status_code=status.HTTP_201_CREATED,
)
async def create_member(
    current_user: Annotated[CurrentUserDTO, Depends(get_current_user)],
    member_service: Annotated[MemberService, Depends(get_member_service)],
    project_id: str,
):
    return await member_service.create(
        MemberCreateDTO(user_id=current_user.id, project_id=project_id)
    )


@router.get(
    "/{project_id}/members/",
    response_model=List[MemberBaseResponse],
    responses={200: {"model": List[MemberBaseResponse]}},
    status_code=status.HTTP_200_OK,
)
async def get_all_members_for_project(
    member_service: Annotated[MemberService, Depends(get_member_service)],
    project_id: str,
    member_status: MemberStatus | None = None,
):
    return await member_service.get_all_for_project(project_id, member_status)
