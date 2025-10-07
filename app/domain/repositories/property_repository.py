from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.property import Property


class PropertyRepository(ABC):
    @abstractmethod
    def add(self, property_arg: Property) -> Property:
        pass

    @abstractmethod
    def get_by_id(self, property_id: int) -> Property:
        pass

    @abstractmethod
    def get_all(self) -> List[Property]:
        pass

    @abstractmethod
    def update(self, property_arg: Property) -> Optional[Property]:
        pass

    @abstractmethod
    def delete(self, property_id: int) -> bool:
        pass
