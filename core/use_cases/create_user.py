from core.domain.entities.user import User
from core.domain.repositories.user_repository import UserRepository

class CreateUser:
  def __init__(self, user_repository: UserRepository):
    self.user_repository = user_repository
  
  def execute(self, user: User) -> User:
    return self.user_repository.add(user)
