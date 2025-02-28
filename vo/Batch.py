from dataclasses import dataclass

from vo import Section

@dataclass
class Batch:
    title: str
    sections: [Section]

    def __init__(self, title: str, sections: [Section]):
        self.title = title
        self.sections = sections

    def __str__(self) -> str:
        return self.title
