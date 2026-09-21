"""
Mini project — Student Gradebook (combines every topic)
=======================================================

GOAL
    Load messy student scores from data/students.csv, reject bad rows with
    clear error messages, build Student objects, and let the user explore
    the results through a menu.

    This file REUSES your earlier work:
        letter_grade  (Topic 2)   clean_name  (Topic 4)   Student  (Topic 7)
    so finish Topics 1–7 first.

The CSV has columns: student_id,name,course,score
Open data/students.csv and look at it before you start — it contains
deliberate problems (blank score, "abc", 105, missing ID, messy spaces).

Run the program:   python ex08_gradebook_project.py
Check your work:   pytest tests/test_ex08_gradebook_project.py -v
"""

import csv
from pathlib import Path

from ex02_conditions_loops import letter_grade
from ex04_collections_strings import clean_name
from ex07_oop import Student

HERE = Path(__file__).parent
DATA_FILE = HERE / "data" / "students.csv"
REPORT_FILE = HERE / "output" / "report.csv"


def load_gradebook(path) -> tuple:
    """Step 1 — Read the CSV and build the gradebook.

    Return (students, errors):
      students -> dict mapping student_id -> Student
                  (one Student per ID; a student with several rows gets
                  several course scores; use clean_name() on names)
      errors   -> list of strings formatted exactly as
                  "line <N>: <reason>"   (header = line 1)
                  where <reason> is one of:
                    "missing student_id"
                    "score is not a number"
                    "score out of range"

    Rules:
      - Only create/store a Student once one of their rows is VALID.
      - Scores may be decimals, so convert with float().
      - Let Student.add_score() do the 0–100 check (catch its ValueError).
      - If the file doesn't exist, let FileNotFoundError propagate —
        main() will handle it.
    """
    students = {}
    errors = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for lineno, row in enumerate(reader, start=2):
            student_id = (row.get("student_id") or "").strip()
            name = row.get("name", "")
            course = row.get("course", "")
            score_raw = row.get("score", "")
            if not student_id:
                errors.append(f"line {lineno}: missing student_id")
                continue
            try:
                score = float(score_raw)
            except Exception:
                errors.append(f"line {lineno}: score is not a number")
                continue
            # If student not yet created, create only when this row is valid
            if student_id not in students:
                student = Student(clean_name(name), student_id)
                try:
                    student.add_score(course, score)
                except ValueError:
                    errors.append(f"line {lineno}: score out of range")
                    continue
                students[student_id] = student
            else:
                try:
                    students[student_id].add_score(course, score)
                except ValueError:
                    errors.append(f"line {lineno}: score out of range")
                    continue
    return (students, errors)


def class_report(students: dict) -> list:
    """Step 2 — Build the report rows.

    Return a list of tuples (student_id, name, average, letter) sorted by
    average (highest first), then by name (A–Z) for ties.
    """
    rows = []
    for sid, student in students.items():
        avg = student.average()
        grade = letter_grade(avg)
        rows.append((sid, student.name, avg, grade))
    # sort by average desc, then name asc
    rows.sort(key=lambda t: (-t[2], t[1]))
    return rows


def find_students(students: dict, query: str) -> list:
    """Step 3 — Case-insensitive search by part of a name.

    Return matching Student objects sorted by name. An empty/blank query
    returns an empty list.
    """
    q = (query or "").strip()
    if not q:
        return []
    ql = q.lower()
    matches = [s for s in students.values() if ql in s.name.lower()]
    return sorted(matches, key=lambda s: s.name)


def save_report(path, report: list) -> None:
    """Step 4 — Save the report as CSV with header
    student_id,name,average,grade
    Create the parent folder if it doesn't exist
    (Path(path).parent.mkdir(parents=True, exist_ok=True)).
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["student_id", "name", "average", "grade"])
        for row in report:
            # ensure average is written as string/number
            writer.writerow([row[0], row[1], row[2], row[3]])


def main() -> None:
    """Step 5 — The menu program (not auto-tested; run the file to try it).

    1. Load the gradebook from DATA_FILE. If the file is missing, print a
       friendly message and return. Print how many students loaded and
       every error message.
    2. Loop over this menu until the user types "q":
         1) Show class report     (print each row neatly aligned)
         2) Show top student
         3) Search by name
         4) Save report to output/report.csv
         q) Quit
    3. Unknown input -> "Unknown option".
    """
    try:
        students, errors = load_gradebook(DATA_FILE)
    except FileNotFoundError:
        print(f"Data file not found: {DATA_FILE}")
        return
    print(f"Loaded {len(students)} students")
    for e in errors:
        print(e)

    while True:
        print("Menu:\n1) Show class report\n2) Show top student\n3) Search by name\n4) Save report\nq) Quit")
        choice = input("Choose an option: ").strip()
        if choice == "q":
            break
        if choice == "1":
            for sid, name, avg, grade in class_report(students):
                print(f"{sid} | {name} | {avg:.2f} | {grade}")
        elif choice == "2":
            report = class_report(students)
            if report:
                sid, name, avg, grade = report[0]
                print(f"Top student: {name} ({sid}) - {avg:.2f} {grade}")
            else:
                print("No students")
        elif choice == "3":
            q = input("Search query: ")
            matches = find_students(students, q)
            for s in matches:
                print(f"{s.name} ({s.student_id}) - avg {s.average():.2f}")
        elif choice == "4":
            report = class_report(students)
            save_report(REPORT_FILE, report)
            print(f"Saved report to {REPORT_FILE}")
        else:
            print("Unknown option")


if __name__ == "__main__":
    main()
