import dataclasses
from pydantic.dataclasses import dataclass

@dataclass
class Labels:
    string_labels: list[str] = dataclasses.field(default_factory=lambda: [])
    date_labels: list[str] = dataclasses.field(default_factory=lambda: [])
    enum_labels: list[str] = dataclasses.field(default_factory=lambda: [])
    boolean_labels: list[str] = dataclasses.field(default_factory=lambda: [])
    integer_labels: list[str] = dataclasses.field(default_factory=lambda: [])