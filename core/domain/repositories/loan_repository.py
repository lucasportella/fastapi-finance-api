from abc import ABC, abstractmethod
from typing import List, Optional
from core.domain.entities.loan import Loan

class LoanRepository(ABC):
  @abstractmethod
  def add(self, loan: Loan) -> Loan:
    pass
  
  @abstractmethod
  def get_all(self) -> List[Loan]:
    pass
  
  @abstractmethod
  def get_by_id(self, loan_id: int) -> Optional[Loan]:
    pass
  
  @abstractmethod
  def update(self, loan: Loan) -> Optional[Loan]:
    pass
  
  @abstractmethod
  def delete(self, loan_id: int) -> bool:
    pass