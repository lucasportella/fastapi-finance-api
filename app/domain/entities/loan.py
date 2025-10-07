from dataclasses import dataclass

from user import Asset


class Collateral(Asset):
    contractId: str
    contract: str


@dataclass
class Loan:
    type: str
    net_loan: float
    interest_rate: float
    total_installments: int
    principal_paid: float
    remaining: float
    down_payment: float
    score_risk: float
