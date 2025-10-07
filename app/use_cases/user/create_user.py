from dataclasses import asdict

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.presentation.dtos.user_dto import UserCreateDTO
from app.presentation.schemas.user_schema import UserResponse


class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def from_dto(self, user_dto: UserCreateDTO) -> User:
        return User(**asdict(user_dto))

    def execute(self, user: User) -> UserResponse:
        created_user = self.user_repository.add(user)
        return UserResponse.from_domain(created_user)
