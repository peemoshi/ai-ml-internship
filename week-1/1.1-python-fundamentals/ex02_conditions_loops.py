"""
Topic 2 — Conditions and loops
==============================

WHAT THIS TOPIC SOLVES
    Conditions (if / elif / else) let a program make decisions.
    Loops repeat work: `for` when you know what to loop over,
    `while` when you repeat until something becomes true.

WORKED EXAMPLE
"""


def count_positives(numbers: list) -> int:
    """Count how many numbers in the list are greater than zero.

    >>> count_positives([3, -1, 0, 8])
    2
    """
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count


# ---------------------------------------------------------------------------
# EXERCISES — check with:   pytest tests/test_ex02_conditions_loops.py -v
# ---------------------------------------------------------------------------


def letter_grade(score: float) -> str:
    """Exercise 2.1 — Grade calculator.

    90–100 -> "A", 80–89 -> "B", 70–79 -> "C", 60–69 -> "D", 0–59 -> "F".
    Any score below 0 or above 100 -> "Invalid".

    >>> letter_grade(85)
    'B'
    >>> letter_grade(105)
    'Invalid'
    """
    # TODO: write your code here
    raise NotImplementedError


def analyze_numbers(numbers: list) -> dict:
    """Exercise 2.2 — Number analyzer.

    Return a dict with keys: "count", "total", "minimum", "maximum",
    "evens", "odds".

    RULE: do NOT use the built-ins sum(), min(), max() or len() here —
    the point is to practise writing the loop yourself.
    For an empty list, minimum and maximum should be None.

    >>> analyze_numbers([4, 7, 1])
    {'count': 3, 'total': 12, 'minimum': 1, 'maximum': 7, 'evens': 1, 'odds': 2}
    """
    # TODO: write your code here
    raise NotImplementedError


def fizzbuzz(n: int) -> list:
    """Exercise 2.3 — Classic FizzBuzz from 1 to n (inclusive), as strings.

    Multiples of 3 -> "Fizz", of 5 -> "Buzz", of both -> "FizzBuzz",
    otherwise the number itself as a string.

    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']
    """
    # TODO: write your code here
    raise NotImplementedError


def triangle_pattern(height: int) -> str:
    """Exercise 2.4 — Pattern generator.

    Return a right-angled triangle of '*' with `height` rows, rows joined
    by newline characters (no trailing newline). Height 0 -> empty string.

    >>> print(triangle_pattern(3))
    *
    **
    ***
    """
    # TODO: write your code here
    raise NotImplementedError


def digit_sum(n: int) -> int:
    """Exercise 2.5 — Sum the digits of a non-negative integer using a WHILE loop.

    Do not convert the number to a string. Hint: n % 10 gives the last digit,
    n // 10 removes it.

    >>> digit_sum(1234)
    10
    """
    # TODO: write your code here
    raise NotImplementedError


def menu_program() -> None:
    """Exercise 2.6 — Menu program (not auto-tested: run this file to try it).

    Show this menu in a loop until the user types "q":
        1) Letter grade for a score
        2) FizzBuzz up to N
        3) Triangle of height N
        q) Quit
    Call your functions above for each option. If the user types anything
    else, print "Unknown option" and show the menu again.
    """
    # TODO: write your code here
    raise NotImplementedError


if __name__ == "__main__":
    print("Worked example:", count_positives([3, -1, 0, 8]))
    menu_program()
