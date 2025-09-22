from abc import ABC,abstractmethod
from typing import List, Optional
from app.domain.entities.property import property

class PropertyRepository(ABC):
  @abstractmethod
  def add(self, property: property) -> property:
    pass

  @abstractmethod
  def get_by_id(self, property_id: int) -> property:
    pass
  
  @abstractmethod
  def get_all(self) -> List[property]:
    pass
  
  @abstractmethod
  def update(self, property: property) -> Optional[property]:
    pass

  @abstractmethod
  def delete(self, property_id: int) -> bool:
    pass