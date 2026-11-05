

import pytest

from app.models.developer import Developer
from app.services.developer_service import display_developer_info, get_active_skills



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


def test_get_active_skills_with_only_cobol() -> None:
    assert get_active_skills(["COBOL"]) == []


def test_get_active_skills_rejects_non_list() -> None:
    with pytest.raises(TypeError, match="Skills must be a list"):
        get_active_skills("Java")


def test_get_active_skills_rejects_non_string_skill() -> None:
    with pytest.raises(TypeError, match="Every skill must be a string"):
        get_active_skills(["Java", 123])


def test_display_developer_info_with_empty_skills(capsys) -> None:
    developer = Developer(name="Alex", experience_years=5, skills=[])

    display_developer_info(developer)

    assert capsys.readouterr().out == (
        "Developer Name: Alex\n"
        "Experience Years: 5\n"
        "Skills: \n"
    )