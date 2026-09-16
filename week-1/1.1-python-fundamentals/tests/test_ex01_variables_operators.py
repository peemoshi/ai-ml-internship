from ex01_variables_operators import (
    average_of_three, format_student_card, is_even, seconds_to_hms, split_bill,
)


def test_seconds_to_hms():
    assert seconds_to_hms(3725) == (1, 2, 5)
    assert seconds_to_hms(59) == (0, 0, 59)
    assert seconds_to_hms(0) == (0, 0, 0)
    assert seconds_to_hms(86400) == (24, 0, 0)


def test_average_of_three():
    assert average_of_three(70, 85, 90) == 81.67
    assert average_of_three(1, 2, 3) == 2.0


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True
    assert is_even(-3) is False


def test_split_bill():
    assert split_bill(300, 4) == 82.5
    assert split_bill(100, 3, tip_percent=0) == 33.33
    assert split_bill(50, 1, tip_percent=20) == 60.0


def test_format_student_card():
    assert format_student_card("Aru", 20, 3.7) == "Name: Aru | Age: 20 | GPA: 3.70"
    assert format_student_card("Dana", 19, 4) == "Name: Dana | Age: 19 | GPA: 4.00"
