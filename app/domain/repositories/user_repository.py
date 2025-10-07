from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.user import User


class UserRepository(ABC):

    @abstractmethod
    def add(self, user: User) -> User: ...

    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[User]: ...

    @abstractmethod
    def get_all(self) -> List[User]: ...

    @abstractmethod
    def update(self, user: User) -> Optional[User]: ...

    @abstractmethod
    def delete(self, user_id: str) -> bool: ...
