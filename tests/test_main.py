

from app.developer import get_active_skills


def test_get_active_skills_removes_cobol() -> None:
    skills = ["Java", "COBOL", "Python"]

    result = get_active_skills(skills)

    assert result == ["Java", "Python"]


def test_get_active_skills_with_no_cobol() -> None:
    skills = ["Java", "Python", "AWS"]

    result = get_active_skills(skills)

    assert result == ["Java", "Python", "AWS"]


def test_get_active_skills_with_empty_list() -> None:
    skills = []

    result = get_active_skills(skills)

    assert result == []