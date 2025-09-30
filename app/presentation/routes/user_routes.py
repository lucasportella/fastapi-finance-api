from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.domain.entities.user import User
from app.use_cases.user.create_user import CreateUser
from app.presentation.routes.dependencies.user_dependencies import create_user_case
from app.use_cases.user.get_all_users import GetAllUsers
from app.presentation.routes.dependencies.user_dependencies import get_all_user_case
from app.use_cases.user.delete_user import DeleteUser
from app.presentation.routes.dependencies.user_dependencies import delete_user_case

router = APIRouter()

class APIResponse(BaseModel):
  status: str
  message: str
  data: dict | None = None

# TODO: change Domain models to pydantic
@router.get('/users', response_model=APIResponse)
def get_all_users_endpoint(use_case: GetAllUsers = Depends(get_all_user_case)):
  users = use_case.execute()
  return APIResponse(
    status='success',
    message='Users retrieved',
    data={'users': users},
  )

@router.post('/create', response_model=APIResponse)
def create_user_endpoint(user: User, use_case: CreateUser = Depends(create_user_case)):
  createdUser = use_case.execute(user)
  return APIResponse(
    status='success' if createdUser.id else 'error',
    message=f'User {createdUser.id} created' if createdUser.id else 'User not created',
    data={**createdUser.__dict__}
  )



@router.delete('/delete/{userId}', response_model=APIResponse)
def delete_user_endpoint(userId: str, use_case: DeleteUser = Depends(delete_user_case)):
  deleted =  use_case.execute(userId)
  return APIResponse(
    status='success' if deleted else 'error',
    message=f'User {userId} deleted' if deleted else 'User not found or already deleted',
  )