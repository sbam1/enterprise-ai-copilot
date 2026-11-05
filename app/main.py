from app.models.developer import Developer
from app.services.developer_service import display_developer_info


def main() -> None:
    developer1 = Developer(
        name="Suseel",
        experience_years=13,
        skills=["Java", "Spring Boot", "AWS", "COBOL"],
    )

    developer2 = Developer(
        name="Syam",
        experience_years=13,
    )

    developers: list[Developer] = [developer1, developer2]

    for developer in developers:
        display_developer_info(developer)


if __name__ == "__main__":
    main()