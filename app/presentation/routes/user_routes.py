from fastapi import APIRouter, Depends
from app.domain.entities.user import User
from app.use_cases.create_user import CreateUser
from app.infrastructure.database.mongo_user_repository import MongoUserRepository
from app.presentation.routes.dependencies.user_dependencies import get_create_user_case

router = APIRouter()

@router.post('/users', response_model=User)
def create_user_endpoint(user: User, use_case: CreateUser = Depends(get_create_user_case)):
  return use_case.execute(user)