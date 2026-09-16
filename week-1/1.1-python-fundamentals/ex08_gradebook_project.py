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
    # TODO: write your code here
    raise NotImplementedError


def class_report(students: dict) -> list:
    """Step 2 — Build the report rows.

    Return a list of tuples (student_id, name, average, letter) sorted by
    average (highest first), then by name (A–Z) for ties.
    """
    # TODO: write your code here
    raise NotImplementedError


def find_students(students: dict, query: str) -> list:
    """Step 3 — Case-insensitive search by part of a name.

    Return matching Student objects sorted by name. An empty/blank query
    returns an empty list.
    """
    # TODO: write your code here
    raise NotImplementedError


def save_report(path, report: list) -> None:
    """Step 4 — Save the report as CSV with header
    student_id,name,average,grade
    Create the parent folder if it doesn't exist
    (Path(path).parent.mkdir(parents=True, exist_ok=True)).
    """
    # TODO: write your code here
    raise NotImplementedError


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
    # TODO: write your code here
    raise NotImplementedError


if __name__ == "__main__":
    main()
