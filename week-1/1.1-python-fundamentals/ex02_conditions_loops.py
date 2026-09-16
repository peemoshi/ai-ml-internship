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
    if score < 0 or score > 100:
        return "Invalid"
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


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
    count = 0
    total = 0
    minimum = None
    maximum = None
    evens = 0
    odds = 0
    for num in numbers:
        count += 1
        total += num
        if minimum is None or num < minimum:
            minimum = num
        if maximum is None or num > maximum:
            maximum = num
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    return {
        "count": count,
        "total": total,
        "minimum": minimum,
        "maximum": maximum,
        "evens": evens,
        "odds": odds,
    }


def fizzbuzz(n: int) -> list:
    """Exercise 2.3 — Classic FizzBuzz from 1 to n (inclusive), as strings.

    Multiples of 3 -> "Fizz", of 5 -> "Buzz", of both -> "FizzBuzz",
    otherwise the number itself as a string.

    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def triangle_pattern(height: int) -> str:
    """Exercise 2.4 — Pattern generator.

    Return a right-angled triangle of '*' with `height` rows, rows joined
    by newline characters (no trailing newline). Height 0 -> empty string.

    >>> print(triangle_pattern(3))
    *
    **
    ***
    """
    if height <= 0:
        return ""
    lines = ["*" * i for i in range(1, height + 1)]
    return "\n".join(lines)


def digit_sum(n: int) -> int:
    """Exercise 2.5 — Sum the digits of a non-negative integer using a WHILE loop.

    Do not convert the number to a string. Hint: n % 10 gives the last digit,
    n // 10 removes it.

    >>> digit_sum(1234)
    10
    """
    total = 0
    if n == 0:
        return 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


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
    while True:
        print("Menu:\n1) Letter grade for a score\n2) FizzBuzz up to N\n3) Triangle of height N\nq) Quit")
        choice = input("Choose an option: ").strip()
        if choice == "q":
            break
        if choice == "1":
            try:
                score = float(input("Score (0-100): "))
            except ValueError:
                print("Invalid input")
                continue
            print(letter_grade(score))
        elif choice == "2":
            try:
                n = int(input("N: "))
            except ValueError:
                print("Invalid input")
                continue
            print("\n".join(fizzbuzz(n)))
        elif choice == "3":
            try:
                h = int(input("Height: "))
            except ValueError:
                print("Invalid input")
                continue
            print(triangle_pattern(h))
        else:
            print("Unknown option")


if __name__ == "__main__":
    print("Worked example:", count_positives([3, -1, 0, 8]))
    menu_program()
