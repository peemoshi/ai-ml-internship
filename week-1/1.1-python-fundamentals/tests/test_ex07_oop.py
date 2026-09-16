import pytest

from ex07_oop import Course, ExchangeStudent, Student


def test_student_basics():
    s = Student("Aru", "S001")
    assert (s.name, s.student_id, s.scores) == ("Aru", "S001", {})
    assert s.average() == 0.0
    s.add_score("Python", 88)
    s.add_score("Statistics", 89)
    assert s.average() == 88.5
    assert str(s) == "Aru (S001) - avg 88.50"


def test_add_score_overwrites_and_validates():
    s = Student("Aru", "S001")
    s.add_score("Python", 50)
    s.add_score("Python", 70)
    assert s.scores == {"Python": 70}
    with pytest.raises(ValueError):
        s.add_score("Math", 101)
    with pytest.raises(ValueError):
        s.add_score("Math", -5)
    assert "Math" not in s.scores


def test_exchange_student():
    e = ExchangeStudent("Lucas", "S009", "University of Barcelona")
    assert isinstance(e, Student)
    assert e.home_university == "University of Barcelona"
    e.add_score("AI", 90)
    assert str(e) == "Lucas (S009) - avg 90.00 [exchange: University of Barcelona]"


def test_course_enrollment():
    course = Course("AIE1001", capacity=2)
    aru, dana, mei = Student("Aru", "S1"), Student("Dana", "S2"), Student("Mei", "S3")
    assert course.enroll(dana) is True
    assert course.enroll(aru) is True
    assert course.enroll(mei) is False            # full
    assert len(course) == 2
    assert course.roster() == ["Aru", "Dana"]


def test_course_rejects_duplicate_id():
    course = Course("AIE1001", capacity=5)
    assert course.enroll(Student("Aru", "S1")) is True
    assert course.enroll(Student("Aru again", "S1")) is False
    assert len(course) == 1
