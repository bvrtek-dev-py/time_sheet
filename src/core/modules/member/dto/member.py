from typing import Optional

from pydantic import BaseModel, Field


class MemberDTO(BaseModel):
    id: Optional[str] = Field(alias="_id")
    user_id: str
    project_id: str
    status: str
