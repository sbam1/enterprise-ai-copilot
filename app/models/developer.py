from dataclasses import dataclass


@dataclass
class Developer:
    name: str
    experience_years: int
    skills: list[str] | None = None