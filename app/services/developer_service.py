from app.models.developer import Developer


def get_active_skills(skills: list[str]) -> list[str]:
    if not isinstance(skills, list):
        raise TypeError("Skills must be a list")

    if not all(isinstance(skill, str) for skill in skills):
        raise TypeError("Every skill must be a string")

    return [skill for skill in skills if skill != "COBOL"]


def display_developer_info(developer: Developer) -> None:
    print(f"Developer Name: {developer.name}")
    print(f"Experience Years: {developer.experience_years}")

    if developer.skills is None:
        print("Skills: Not provided")
    else:
        active_skills = get_active_skills(developer.skills)
        print(f"Skills: {', '.join(active_skills)}")