import dataclasses
from pydantic.dataclasses import dataclass

@dataclass
class DateField:
    type: str = "string"
    format: str = "date"