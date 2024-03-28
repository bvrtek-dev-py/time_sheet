from pydantic import model_validator

from time_sheet.src.core.modules.common.models.base_model import MongoDBModel
from time_sheet.src.infrastructure.ports.api.v1.common.validators import (
    validate_object_id_type,
)


class Member(MongoDBModel):
    user_id: str
    project_id: str
    status: str

    @model_validator(mode="after")
    def validate_user_and_project_id(self):
        validate_object_id_type(self.user_id)
        validate_object_id_type(self.project_id)
