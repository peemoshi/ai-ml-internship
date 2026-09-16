"""
Topic 3 — Functions
===================

WHAT THIS TOPIC SOLVES
    Functions package logic you use more than once behind a clear name.
    Good functions take inputs as parameters, return a result, and do not
    secretly change global variables or the objects you pass in.

    Key ideas: parameters, return values, default arguments,
    *args (any number of positional arguments), **kwargs (any number of
    named arguments), and not mutating inputs.

WORKED EXAMPLE
"""


def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting. `greeting` has a default value.

    >>> greet("Aru")
    'Hello, Aru!'
    >>> greet("Aru", greeting="Salem")
    'Salem, Aru!'
    """
    return f"{greeting}, {name}!"


# ---------------------------------------------------------------------------
# EXERCISES — check with:   pytest tests/test_ex03_functions.py -v
# ---------------------------------------------------------------------------


def final_grade(assignments: list, exam: float, assignment_weight: float = 0.4) -> float:
    """Exercise 3.1 — Weighted final grade.

    final = (average of assignments) * assignment_weight
            + exam * (1 - assignment_weight)
    Round to 2 decimals.

    >>> final_grade([80, 90, 100], 70)       # 90*0.4 + 70*0.6
    78.0
    """
    if assignments:
        avg_assignments = sum(assignments) / len(assignments)
    else:
        avg_assignments = 0
    final = avg_assignments * assignment_weight + exam * (1 - assignment_weight)
    return round(final, 2)


def apply_curve(scores: list, bonus: float = 5, cap: float = 100) -> list:
    """Exercise 3.2 — Add `bonus` to every score, never going above `cap`.

    IMPORTANT: return a NEW list. The original `scores` list must not change.

    >>> apply_curve([90, 97, 60])
    [95, 100, 65]
    """
    new_scores = []
    for s in scores:
        bumped = s + bonus
        if bumped > cap:
            bumped = cap
        new_scores.append(bumped)
    return new_scores


def mean(*values: float):
    """Exercise 3.3 — Average of any number of arguments (uses *args).

    Return None when called with no arguments.

    >>> mean(2, 4, 9)
    5.0
    >>> mean() is None
    True
    """
    if not values:
        return None
    return sum(values) / len(values)


def subject_report(name: str, **scores: float) -> str:
    """Exercise 3.4 — Build a report from named scores (uses **kwargs).

    Subjects must be listed in alphabetical order.
    If no scores are given, return "<name>: no scores".

    >>> subject_report("Aru", physics=85, math=90)
    'Aru: math=90, physics=85'
    >>> subject_report("Dana")
    'Dana: no scores'
    """
    if not scores:
        return f"{name}: no scores"
    parts = []
    for subject in sorted(scores.keys()):
        v = scores[subject]
        if isinstance(v, float) and v.is_integer():
            v_str = str(int(v))
        else:
            v_str = str(v)
        parts.append(f"{subject}={v_str}")
    return f"{name}: " + ", ".join(parts)


def is_palindrome(text: str) -> bool:
    """Exercise 3.5 — Palindrome check that ignores case, spaces and punctuation.

    Hint: build a cleaned string first using str.isalnum() and str.lower(),
    then compare it with its reverse (slicing: s[::-1]).

    >>> is_palindrome("Never odd or even")
    True
    >>> is_palindrome("Python")
    False
    """
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(greet("Aru"))
    print(greet("Aru", greeting="Salem"))
