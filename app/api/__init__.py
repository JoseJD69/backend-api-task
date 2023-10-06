from fastapi import APIRouter
from app.api.v1.GitHub.handler import general_router

app_router = APIRouter()
# version 1
# Auth routes
app_router.include_router(general_router, prefix="/github", tags=["github"])
