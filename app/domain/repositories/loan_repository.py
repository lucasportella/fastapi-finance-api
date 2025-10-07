from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.loan import Loan


class LoanRepository(ABC):
    @abstractmethod
    def add(self, loan: Loan) -> Loan: ...

    @abstractmethod
    def get_all(self) -> List[Loan]: ...

    @abstractmethod
    def get_by_id(self, loan_id: int) -> Optional[Loan]: ...

    @abstractmethod
    def update(self, loan: Loan) -> Optional[Loan]: ...

    @abstractmethod
    def delete(self, loan_id: int) -> bool: ...
