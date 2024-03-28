from typing import Annotated, List

from fastapi import APIRouter, Depends
from starlette import status

from time_sheet.src.application.modules.member.services.member_service import (
    MemberService,
)
from time_sheet.src.core.modules.auth.dto.auth import CurrentUserDTO
from time_sheet.src.infrastructure.dependencies.auth.permissions import get_current_user
from time_sheet.src.infrastructure.dependencies.member.factories import (
    get_member_service,
)
from time_sheet.src.infrastructure.ports.api.v1.common.responses import ErrorResponse
from time_sheet.src.infrastructure.ports.api.v1.member.requests import (
    MemberUpdateRequest,
)
from time_sheet.src.infrastructure.ports.api.v1.member.responses import (
    MemberBaseResponse,
)

router = APIRouter(prefix="/api/v1/members", tags=["APIv1 Members"])


@router.patch(
    "/members/{member_id}",
    response_model=MemberBaseResponse,
    responses={200: {"model": MemberBaseResponse}},
    status_code=status.HTTP_200_OK,
)
async def patch_member(
    member_service: Annotated[MemberService, Depends(get_member_service)],
    request: MemberUpdateRequest,
    member_id: str,
):
    return await member_service.update(member_id, request.status)


@router.delete(
    "/members/{member_id}",
    responses={204: {"model": None}, 404: {"model": ErrorResponse}},
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_member(
    member_service: Annotated[MemberService, Depends(get_member_service)],
    member_id: str,
):
    return await member_service.delete(member_id)


@router.get(
    "/members/participates",
    response_model=List[MemberBaseResponse],
    responses={200: {"model": List[MemberBaseResponse]}},
    status_code=status.HTTP_200_OK,
)
async def get_participates(
    current_user: Annotated[CurrentUserDTO, Depends(get_current_user)],
    member_service: Annotated[MemberService, Depends(get_member_service)],
):
    return await member_service.get_participates(current_user.id)
