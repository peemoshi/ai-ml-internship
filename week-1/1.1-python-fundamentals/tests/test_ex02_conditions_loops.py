import pytest

from ex02_conditions_loops import analyze_numbers, digit_sum, fizzbuzz, letter_grade, triangle_pattern


@pytest.mark.parametrize("score, expected", [
    (100, "A"), (90, "A"), (89.9, "B"), (80, "B"), (75, "C"),
    (60, "D"), (59, "F"), (0, "F"), (-1, "Invalid"), (101, "Invalid"),
])
def test_letter_grade(score, expected):
    assert letter_grade(score) == expected


def test_analyze_numbers():
    assert analyze_numbers([4, 7, 1]) == {
        "count": 3, "total": 12, "minimum": 1, "maximum": 7, "evens": 1, "odds": 2,
    }
    assert analyze_numbers([-5, -2]) == {
        "count": 2, "total": -7, "minimum": -5, "maximum": -2, "evens": 1, "odds": 1,
    }


def test_analyze_numbers_empty():
    assert analyze_numbers([]) == {
        "count": 0, "total": 0, "minimum": None, "maximum": None, "evens": 0, "odds": 0,
    }


def test_fizzbuzz():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    assert fizzbuzz(0) == []


def test_triangle_pattern():
    assert triangle_pattern(3) == "*\n**\n***"
    assert triangle_pattern(1) == "*"
    assert triangle_pattern(0) == ""


def test_digit_sum():
    assert digit_sum(1234) == 10
    assert digit_sum(0) == 0
    assert digit_sum(9) == 9
