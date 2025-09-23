from fastapi import APIRouter, Depends
from app.domain.entities.user import User
from app.use_cases.user.create_user import CreateUser
from app.presentation.routes.dependencies.user_dependencies import get_create_user_case
from app.use_cases.user.get_all_users import GetAllUsers
from app.presentation.routes.dependencies.user_dependencies import get_all_user_case
from typing import List

router = APIRouter()

@router.get('/users', response_model= List[User])
def get_all_users_endpoint(use_case: GetAllUsers = Depends(get_all_user_case)):
  return use_case.execute()

@router.post('/create-user', response_model=User)
def create_user_endpoint(user: User, use_case: CreateUser = Depends(get_create_user_case)):
  return use_case.execute(user)