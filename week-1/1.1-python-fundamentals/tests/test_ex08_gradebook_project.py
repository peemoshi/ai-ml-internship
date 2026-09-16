import csv

import pytest

from ex08_gradebook_project import DATA_FILE, class_report, find_students, load_gradebook, save_report


@pytest.fixture
def gradebook():
    return load_gradebook(DATA_FILE)


def test_loads_valid_students(gradebook):
    students, _ = gradebook
    assert sorted(students) == ["S001", "S002", "S003", "S004", "S005"]
    assert students["S001"].name == "Aru Nurlanovna"
    assert students["S002"].name == "Dana Sadykova"
    assert students["S001"].scores == {"Python": 88.0, "Statistics": 92.0}
    assert students["S004"].scores == {"Statistics": 87.0}


def test_reports_bad_rows(gradebook):
    _, errors = gradebook
    assert errors == [
        "line 5: score is not a number",
        "line 6: score is not a number",
        "line 8: score out of range",
        "line 10: missing student_id",
    ]


def test_student_only_created_from_valid_row(tmp_path):
    path = tmp_path / "s.csv"
    path.write_text("student_id,name,course,score\nS9,Ghost,AI,abc\n", encoding="utf-8")
    students, errors = load_gradebook(path)
    assert students == {}
    assert errors == ["line 2: score is not a number"]


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        load_gradebook("definitely_missing.csv")


def test_class_report(gradebook):
    students, _ = gradebook
    assert class_report(students) == [
        ("S002", "Dana Sadykova", 95.0, "A"),
        ("S001", "Aru Nurlanovna", 90.0, "A"),
        ("S004", "Mei Chan", 87.0, "B"),
        ("S003", "Timur Akhmetov", 71.0, "C"),
        ("S005", "Lucas Martin", 61.25, "D"),
    ]


def test_find_students(gradebook):
    students, _ = gradebook
    assert [s.name for s in find_students(students, "AR")] == ["Aru Nurlanovna", "Lucas Martin"]
    assert find_students(students, "zzz") == []
    assert find_students(students, "   ") == []


def test_save_report(tmp_path):
    path = tmp_path / "nested" / "report.csv"
    save_report(path, [("S1", "Aru", 90.0, "A")])
    with open(path, newline="", encoding="utf-8") as f:
        assert list(csv.reader(f)) == [["student_id", "name", "average", "grade"], ["S1", "Aru", "90.0", "A"]]
