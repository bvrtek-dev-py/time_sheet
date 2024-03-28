from time_sheet.src.application.modules.project.dto.project import (
    ProjectGetDTO,
    ProjectWithOwnerDTO,
)


class ProjectDTOToGetMapper:
    def map(self, dto: ProjectWithOwnerDTO) -> ProjectGetDTO:
        return ProjectGetDTO(**dto.model_dump())
