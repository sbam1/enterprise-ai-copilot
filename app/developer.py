from dataclasses import dataclass


@dataclass
class Developer:
    name: str
    experience_years: int
    skills: list[str] | None = None


def get_active_skills(skills: list[str]) -> list[str]:
    active_skills = []

    for skill in skills:
        if skill != "COBOL":
            active_skills.append(skill)

    return active_skills


def display_developer_info(developer: Developer) -> None:
    print(f"Developer Name: {developer.name}")
    print(f"Experience Years: {developer.experience_years}")

    if developer.skills is None:
        print("Skills: Not provided")
    else:
        active_skills = get_active_skills(developer.skills)
        print(f"Skills: {', '.join(active_skills)}")