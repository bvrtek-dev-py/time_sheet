from typing import List

from bson import ObjectId
from motor.core import AgnosticCollection, AgnosticClientSession

from time_sheet.src.core.modules.member.dto.member import MemberDTO
from time_sheet.src.core.modules.member.enum.member_status import MemberStatus
from time_sheet.src.core.modules.member.models.member import Member
from time_sheet.src.core.modules.member.repositories.member_repository import (
    IMemberRepository,
)


class MemberRepository(IMemberRepository):
    def __init__(self, session: AgnosticClientSession):
        self._session: AgnosticCollection = session.client.get_database()[  # type: ignore
            "members"
        ]

    async def save(self, member: MemberDTO) -> MemberDTO:
        model = Member(**member.model_dump())
        result = await self._session.insert_one(model.model_dump(exclude={"id"}))
        member.id = str(result.inserted_id)

        return member

    async def update(self, member: MemberDTO) -> MemberDTO:
        await self._session.update_one(
            {"_id": ObjectId(member.id)}, {"$set": member.model_dump(exclude={"id"})}
        )

        return member

    async def delete(self, member_id: str) -> None:
        await self._session.delete_one({"_id": ObjectId(member_id)})

    async def get_all_for_project(
        self, project_id: str, status: MemberStatus | None = None
    ) -> List[MemberDTO]:
        query = {"project_id": project_id}
        if status is not None:
            query["status"] = status.value
        documents = await self._session.find(query).to_list(length=None)

        return [
            MemberDTO(**document | {"_id": str(document["_id"])})
            for document in documents
        ]

    async def get_by_id(self, member_id: str) -> MemberDTO | None:
        document = await self._session.find_one({"_id": ObjectId(member_id)})

        return (
            MemberDTO(**document | {"_id": str(document["_id"])}) if document else None
        )

    async def get_by_user_id(self, user_id: str) -> List[MemberDTO]:
        documents = await self._session.find({"user_id": user_id}).to_list(length=None)

        return [
            MemberDTO(**document | {"_id": str(document["_id"])})
            for document in documents
        ]
