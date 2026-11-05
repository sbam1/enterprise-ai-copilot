from app.main import main


def test_main(capsys):
    main()

    captured = capsys.readouterr()

    assert "Developer Name: Suseel" in captured.out
    assert "Experience Years: 13" in captured.out
    assert "Java, Spring Boot, AWS" in captured.out
    assert "COBOL" not in captured.out
    assert "Skills: Not provided" in captured.out