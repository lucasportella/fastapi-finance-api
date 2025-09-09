from dataclasses import dataclass
from user import Asset

class Collateral(Asset):
  contractId: str
  contract: str

@dataclass
class Loan:
  type: str
  netLoan: float
  interestRate: float
  totalInstallments: int
  principalPaid: float
  remaining: float
  downPayment: float
  scoreRisk: float
  