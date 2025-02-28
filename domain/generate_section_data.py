from vo.Batch import Batch
from vo.Department import Department
from vo.Section import Section


def generate_section_data():
    it_department = Department(
        title="B.Sc (IT)",
        batches=[
            Batch(
                title="2022-2025",
                sections=[
                    Section(
                        title="1"
                    ),
                    Section(
                        title="2"
                    ),
                ]
            ),
            Batch(
                title="2023-2026",
                sections=[
                    Section(
                        title="1"
                    ),
                    Section(
                        title="2"
                    )
                ]
            ),
            Batch(
                title="2024-2027",
                sections=[
                    Section(
                        title="1"
                    ),
                    Section(
                        title="2"
                    ),
                    Section(
                        title="3"
                    ),
                ]
            )
        ]
    )

    return [it_department]