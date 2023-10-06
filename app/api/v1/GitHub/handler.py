import inject
from fastapi import APIRouter, HTTPException
from loguru import logger

from app.api.v1.GitHub.schemas import RepoCommitsRequest
from app.usecases.ListRepositoriesUseCase import ListRepositoriesUseCase

general_router = APIRouter()


@general_router.get("/repositories")
async def get_repositories():
    use_case: ListRepositoriesUseCase = inject.instance(ListRepositoriesUseCase)
    try:
        return use_case.execute()
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=409, detail=str(e))


@general_router.get("/repository/commits")
async def get_repositories(request: RepoCommitsRequest):
    use_case: ListRepositoriesUseCase = inject.instance(ListRepositoriesUseCase)
    try:
        return use_case.execute()
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=409, detail=str(e))
