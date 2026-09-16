from ex03_functions import apply_curve, final_grade, is_palindrome, mean, subject_report


def test_final_grade():
    assert final_grade([80, 90, 100], 70) == 78.0
    assert final_grade([50], 100, assignment_weight=0.5) == 75.0


def test_apply_curve_values():
    assert apply_curve([90, 97, 60]) == [95, 100, 65]
    assert apply_curve([10, 20], bonus=10, cap=25) == [20, 25]


def test_apply_curve_does_not_modify_input():
    original = [90, 97, 60]
    apply_curve(original)
    assert original == [90, 97, 60]


def test_mean():
    assert mean(2, 4, 9) == 5.0
    assert mean(7) == 7
    assert mean() is None


def test_subject_report():
    assert subject_report("Aru", physics=85, math=90) == "Aru: math=90, physics=85"
    assert subject_report("Dana") == "Dana: no scores"


def test_is_palindrome():
    assert is_palindrome("Never odd or even") is True
    assert is_palindrome("A man, a plan, a canal: Panama!") is True
    assert is_palindrome("Python") is False
    assert is_palindrome("") is True
