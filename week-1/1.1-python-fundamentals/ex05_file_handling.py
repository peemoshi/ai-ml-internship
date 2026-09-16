"""
Topic 5 — File handling (text and CSV)
======================================

WHAT THIS TOPIC SOLVES
    Programs need to keep data after they stop running. Files let you save
    and load it. Always open files with `with open(...)` so they are closed
    automatically, and pass `encoding="utf-8"` so non-English text works.

    Modes: "r" read, "w" write (overwrites!), "a" append.
    For CSV files use the built-in `csv` module instead of splitting by commas.

WORKED EXAMPLE
"""

import csv
from pathlib import Path


def count_lines(path: str) -> int:
    """Count the lines in a text file.

    >>> # count_lines("data/notes.txt")  -> e.g. 12
    """
    with open(path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


# ---------------------------------------------------------------------------
# EXERCISES — check with:   pytest tests/test_ex05_file_handling.py -v
# (the tests create temporary files for you, so nothing is left behind)
# ---------------------------------------------------------------------------


def save_notes(path: str, notes: list) -> None:
    """Exercise 5.1 — Write each note on its own line (overwrite the file)."""
    # TODO: write your code here
    raise NotImplementedError


def load_notes(path: str) -> list:
    """Exercise 5.2 — Read notes back as a list of strings without newlines.

    - Skip blank lines.
    - If the file does not exist, return an empty list (do not crash).
      Hint: catch FileNotFoundError specifically.
    """
    # TODO: write your code here
    raise NotImplementedError


def read_scores_csv(path: str) -> tuple:
    """Exercise 5.3 — Read a CSV with columns: name,score

    Return a tuple (valid_rows, bad_lines):
      valid_rows -> list of dicts like {"name": "Aru", "score": 88}
                    (score converted to int, name stripped of spaces)
      bad_lines  -> list of LINE NUMBERS whose score is missing or not a
                    whole number. The header is line 1, so the first data
                    row is line 2.

    Hint: csv.DictReader + enumerate(reader, start=2).
    """
    # TODO: write your code here
    raise NotImplementedError


def write_summary_csv(path: str, averages: dict) -> None:
    """Exercise 5.4 — Write a CSV with header `name,average`, one row per student,
    sorted by name.

    >>> # write_summary_csv("out.csv", {"Mei": 87.7, "Aru": 86.3})
    >>> # out.csv:
    >>> #   name,average
    >>> #   Aru,86.3
    >>> #   Mei,87.7

    Hint: csv.writer, and open the file with newline="".
    """
    # TODO: write your code here
    raise NotImplementedError


def append_log(path: str, message: str) -> int:
    """Exercise 5.5 — Append `message` as a new line to a log file.

    Create the file if it doesn't exist. Return how many lines the file
    has AFTER appending.
    """
    # TODO: write your code here
    raise NotImplementedError


if __name__ == "__main__":
    demo = Path("demo_notes.txt")
    save_notes(demo, ["Learn pandas", "Push to GitHub"])
    print(load_notes(demo))
    print(load_notes("this_file_does_not_exist.txt"))   # should print []
    demo.unlink()
