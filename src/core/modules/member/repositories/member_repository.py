# pylint: disable=R0801
from abc import ABC, abstractmethod
from typing import List

from time_sheet.src.core.modules.member.dto.member import MemberDTO
from time_sheet.src.core.modules.member.enum.member_status import MemberStatus


class IMemberRepository(ABC):
    @abstractmethod
    async def save(self, member: MemberDTO) -> MemberDTO:
        pass

    @abstractmethod
    async def get_all_for_project(
        self, project_id: str, status: MemberStatus | None = None
    ) -> List[MemberDTO]:
        pass

    @abstractmethod
    async def get_by_id(self, member_id: str) -> MemberDTO | None:
        pass

    @abstractmethod
    async def get_by_user_id(self, user_id: str) -> List[MemberDTO]:
        pass

    @abstractmethod
    async def delete(self, member_id: str) -> None:
        pass

    @abstractmethod
    async def update(self, member: MemberDTO) -> MemberDTO:
        pass
