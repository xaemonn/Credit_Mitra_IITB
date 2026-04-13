from pydantic import BaseModel
from typing import Optional, List


class Transaction(BaseModel):
    date: Optional[str]
    amount: Optional[float]
    type: Optional[str]
    balance: Optional[float]
    reference_number: Optional[str]
    category: Optional[str]
    transaction: str


class TransactionList(BaseModel):
    transactions: List[Transaction]
