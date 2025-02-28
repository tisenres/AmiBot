from dataclasses import dataclass

from vo import Batch
from vo import Section


@dataclass
class Department:
    title: str
    batches: [Batch]
    sections: [Section]

    def __init__(self, title: str, batches: [Batch], sections: Section = None):
        self.title = title
        self.batches = batches
        self.sections = sections

    def __str__(self) -> str:
        return self.title
