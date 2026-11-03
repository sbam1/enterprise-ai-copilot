

from app import developer
from app.developer import  display_developer_info


def main() -> None:
    developer1 = developer(
        name="Suseel",
        experience_years=13,
        skills=["Java", "Spring Boot", "AWS", "COBOL"],
    )

    print("Developer 1 Information:")
    print(developer1)

    developer2 = developer(
        name="Syam",
        experience_years=13,
    )

    print("\nDeveloper 2 Information:")
    print(developer2)

    developers: list[developer] = [developer1, developer2]

    for developer in developers:
        display_developer_info(developer)


if __name__ == "__main__":
    main()