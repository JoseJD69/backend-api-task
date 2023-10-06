import inject
from fastapi import APIRouter, HTTPException
from loguru import logger

from app.usecases.GetCommitsByRepo import GetCommitsByRepoUseCase
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


@general_router.get("/repository/commits/{repository_name}")
async def get_repositories(repository_name: str):
    use_case: GetCommitsByRepoUseCase = inject.instance(GetCommitsByRepoUseCase)
    try:
        return use_case.execute(repository_name)
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=409, detail=str(e))
