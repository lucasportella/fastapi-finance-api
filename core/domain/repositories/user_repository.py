from abc import ABC, abstractmethod
from core.domain.entities.user import User
from typing import Optional, List

class UserRepository(ABC):
  
  @abstractmethod
  def add(self, user: User) -> User:
    pass
  
  @abstractmethod
  def get_by_id(self, user_id: int) -> Optional[User]:
    pass
  
  @abstractmethod
  def get_all(self) -> List[User]:
    pass
  
  @abstractmethod
  def update(self, user: User) -> Optional[User]:
    pass
  
  @abstractmethod
  def delete(self, user_id: int) -> bool:
    pass