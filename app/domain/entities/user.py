from typing import TypedDict, Optional, List
from dataclasses import dataclass, field
from datetime import datetime


# TODO: improve classes types(Asset, Income,Expense type field) for restricted strings list
class Asset(TypedDict):
  type: str
  value: float
  description: str
  year: Optional[int]
  id: Optional[int]

class Debt(TypedDict):
  total_value: float
  interest_rate: float
  total_installments: int
  principal_paid: float
  remaining: float

class Income(TypedDict):
  type: str
  netIncome: float
  
class Expense(TypedDict):
  type: str
  net_expense: float
  

@dataclass
class User:
    first_name: str
    last_name: str
    date_of_birth: datetime
    email: str
    address: str
    phone: str
    hashed_password: str
    id: str | None = None
    assets: List[Asset] = field(default_factory=list)
    debts: List[Debt] = field(default_factory=list)
    incomes: List[Income] = field(default_factory=list)
    expenses: List[Expense] = field(default_factory=list)

    def add_asset(self, asset: Asset):
        self.assets.append(asset)

    def add_debt(self, debt: Debt):
        self.debts.append(debt)

    def add_income(self, income: Income):
        self.incomes.append(income)

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)