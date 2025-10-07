from dataclasses import dataclass
from typing import Optional


@dataclass
class Property:
    address: str
    city: str
    state: str
    zip_code: str
    title_deed_record: str
    id: Optional[int]
