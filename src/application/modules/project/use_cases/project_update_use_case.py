from time_sheet.src.application.modules.project.dto.project import (
    ProjectUpdateDTO,
)
from time_sheet.src.application.modules.project.use_cases.project_get_by_id_use_case import (
    ProjectGetByIdUseCase,
)
from time_sheet.src.core.modules.project.dto.project import ProjectDTO
from time_sheet.src.core.modules.project.repositories.project_repository import (
    IProjectRepository,
)


class ProjectUpdateUseCase:
    def __init__(
        self, repository: IProjectRepository, get_by_id_use_case: ProjectGetByIdUseCase
    ):
        self._repository = repository
        self._get_by_id_use_case = get_by_id_use_case

    async def execute(
        self, request_dto: ProjectUpdateDTO, project_id: str
    ) -> ProjectDTO:
        project_dto = await self._get_by_id_use_case.execute(project_id)
        for key, value in request_dto.model_dump().items():
            setattr(project_dto, key, value)

        return await self._repository.update(project_dto)
