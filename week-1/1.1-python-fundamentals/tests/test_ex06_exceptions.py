import pytest

from ex06_exceptions import InvalidScoreError, ask_age, load_config, parse_age, safe_divide, validate_score


def test_safe_divide():
    assert safe_divide(10, 4) == 2.5
    assert safe_divide(1, 0) is None


def test_safe_divide_does_not_hide_type_errors():
    with pytest.raises(TypeError):
        safe_divide("10", 2)


def test_parse_age_valid():
    assert parse_age(" 21 ") == 21
    assert parse_age("0") == 0


@pytest.mark.parametrize("text, message", [
    ("abc", "Age must be a whole number"),
    ("21.5", "Age must be a whole number"),
    ("-1", "Age must be between 0 and 120"),
    ("121", "Age must be between 0 and 120"),
])
def test_parse_age_invalid(text, message):
    with pytest.raises(ValueError, match=message):
        parse_age(text)


def test_validate_score():
    assert validate_score(88.5) == 88.5
    assert validate_score(0) == 0
    with pytest.raises(InvalidScoreError):
        validate_score(101)
    with pytest.raises(TypeError):
        validate_score("90")
    with pytest.raises(TypeError):
        validate_score(True)


def test_invalid_score_error_is_a_value_error():
    assert issubclass(InvalidScoreError, ValueError)


def test_ask_age_retries_then_succeeds():
    answers = iter(["abc", "200", "25"])
    assert ask_age(input_func=lambda prompt: next(answers)) == 25


def test_ask_age_gives_up():
    answers = iter(["x", "y", "z"])
    assert ask_age(attempts=3, input_func=lambda prompt: next(answers)) is None


def test_load_config(tmp_path):
    good = tmp_path / "config.json"
    good.write_text('{"theme": "dark", "retries": 3}', encoding="utf-8")
    assert load_config(good) == {"theme": "dark", "retries": 3}

    assert load_config(tmp_path / "missing.json") == {}

    broken = tmp_path / "broken.json"
    broken.write_text("{not json", encoding="utf-8")
    with pytest.raises(ValueError, match="not valid JSON"):
        load_config(broken)
