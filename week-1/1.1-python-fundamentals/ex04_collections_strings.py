"""
Topic 4 — Lists, tuples, sets, dictionaries and strings
=======================================================

WHAT THIS TOPIC SOLVES
    list   -> ordered, changeable sequence            [80, 92, 75]
    tuple  -> ordered, fixed group of values          ("Aru", 91.5)
    set    -> unordered, no duplicates, fast "in"     {"Math", "AI"}
    dict   -> look up a value by a key                {"Aru": 91.5}
    str    -> text, with many helpful methods (.strip(), .split(), .lower() ...)

MINI PROBLEM: the exercises below all work with student records like these.
"""

STUDENTS = [
    {"name": "Aru", "major": "AI", "scores": [88, 92, 79]},
    {"name": "Dana", "major": "EdTech", "scores": [95, 90, 98]},
    {"name": "Timur", "major": "AI", "scores": [70, 65, 80]},
    {"name": "Mei", "major": "EdTech", "scores": [85, 87, 91]},
]

# WORKED EXAMPLE


def names_in_major(students: list, major: str) -> list:
    """Return the names of students in the given major, in original order.

    >>> names_in_major(STUDENTS, "AI")
    ['Aru', 'Timur']
    """
    return [s["name"] for s in students if s["major"] == major]


# ---------------------------------------------------------------------------
# EXERCISES — check with:   pytest tests/test_ex04_collections_strings.py -v
# ---------------------------------------------------------------------------


def average_scores(students: list) -> dict:
    """Exercise 4.1 — Map each student's name to their average score (1 decimal).

    >>> average_scores(STUDENTS)["Dana"]
    94.3
    """
    # TODO: write your code here
    raise NotImplementedError


def top_student(students: list) -> tuple:
    """Exercise 4.2 — Return (name, average) of the student with the highest average.

    Return None if the list is empty. Reuse average_scores().

    >>> top_student(STUDENTS)
    ('Dana', 94.3)
    """
    # TODO: write your code here
    raise NotImplementedError


def group_by_major(students: list) -> dict:
    """Exercise 4.3 — Map each major to an alphabetically sorted list of names.

    >>> group_by_major(STUDENTS)
    {'AI': ['Aru', 'Timur'], 'EdTech': ['Dana', 'Mei']}
    """
    # TODO: write your code here
    raise NotImplementedError


def course_overlap(courses_a: list, courses_b: list) -> dict:
    """Exercise 4.4 — Compare two students' course lists using SETS.

    Return {"shared": set, "only_a": set, "only_b": set}.
    Duplicates in the input lists should not matter.

    >>> course_overlap(["AI", "Math", "AI"], ["Math", "Design"])["shared"]
    {'Math'}
    """
    # TODO: write your code here
    raise NotImplementedError


def word_frequency(text: str, top_n: int = 3) -> list:
    """Exercise 4.5 — Most common words as a list of (word, count) tuples.

    - Ignore case ("AI" and "ai" are the same word).
    - Remove these punctuation characters: . , ! ? : ;
    - Sort by count (highest first); break ties alphabetically.
    - Return at most `top_n` items.

    >>> word_frequency("AI helps learning. Learning helps AI, and AI helps teachers!", 2)
    [('ai', 3), ('helps', 3)]
    """
    # TODO: write your code here
    raise NotImplementedError


def clean_name(raw: str) -> str:
    """Exercise 4.6 — Tidy a messy name typed by a user.

    Remove extra spaces (leading, trailing and between words) and use
    Title Case.

    >>> clean_name("   aRU    nURLAN ")
    'Aru Nurlan'
    """
    # TODO: write your code here
    raise NotImplementedError


if __name__ == "__main__":
    print("AI students:", names_in_major(STUDENTS, "AI"))
