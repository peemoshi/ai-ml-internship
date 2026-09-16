from ex04_collections_strings import (
    STUDENTS, average_scores, clean_name, course_overlap, group_by_major, top_student, word_frequency,
)


def test_average_scores():
    assert average_scores(STUDENTS) == {"Aru": 86.3, "Dana": 94.3, "Timur": 71.7, "Mei": 87.7}
    assert average_scores([]) == {}


def test_top_student():
    assert top_student(STUDENTS) == ("Dana", 94.3)
    assert top_student([]) is None


def test_group_by_major():
    assert group_by_major(STUDENTS) == {"AI": ["Aru", "Timur"], "EdTech": ["Dana", "Mei"]}


def test_course_overlap():
    result = course_overlap(["AI", "Math", "AI"], ["Math", "Design"])
    assert result == {"shared": {"Math"}, "only_a": {"AI"}, "only_b": {"Design"}}


def test_word_frequency():
    text = "AI helps learning. Learning helps AI, and AI helps teachers!"
    assert word_frequency(text, 2) == [("ai", 3), ("helps", 3)]
    assert word_frequency(text) == [("ai", 3), ("helps", 3), ("learning", 2)]
    assert word_frequency("", 3) == []


def test_clean_name():
    assert clean_name("   aRU    nURLAN ") == "Aru Nurlan"
    assert clean_name("mei") == "Mei"
