"""
Topic 1 — Variables, data types, input/output and operators
============================================================

WHAT THIS TOPIC SOLVES
    Variables give names to values so you can reuse them. Operators let you
    calculate with them: + - * / (true division), // (floor division),
    % (remainder), ** (power), and comparisons like == < >=.

WORKED EXAMPLE (read it, run it, then do the exercises without copying it)
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit, rounded to 1 decimal place.

    >>> celsius_to_fahrenheit(100)
    212.0
    """
    fahrenheit = celsius * 9 / 5 + 32
    return round(fahrenheit, 1)


# ---------------------------------------------------------------------------
# EXERCISES — replace each `raise NotImplementedError` with your own code.
# Check your work with:   pytest tests/test_ex01_variables_operators.py -v
# ---------------------------------------------------------------------------


def seconds_to_hms(total_seconds: int) -> tuple:
    """Exercise 1.1 — Convert a number of seconds into (hours, minutes, seconds).

    Hint: use // (floor division) and % (remainder). No loops needed.

    >>> seconds_to_hms(3725)
    (1, 2, 5)
    >>> seconds_to_hms(59)
    (0, 0, 59)
    """
    hours = total_seconds // 3600
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return (hours, minutes, seconds)


def average_of_three(a: float, b: float, c: float) -> float:
    """Exercise 1.2 — Return the average of three numbers, rounded to 2 decimals.

    >>> average_of_three(70, 85, 90)
    81.67
    """
    avg = (a + b + c) / 3
    return round(avg, 2)


def is_even(n: int) -> bool:
    """Exercise 1.3 — Return True if n is even, otherwise False.

    Hint: the result of a comparison is already a bool — you don't need if/else.

    >>> is_even(4)
    True
    >>> is_even(7)
    False
    """
    return n % 2 == 0


def split_bill(total: float, people: int, tip_percent: float = 10) -> float:
    """Exercise 1.4 — Add a tip to the bill, then split it equally.

    Return the amount each person pays, rounded to 2 decimals.

    >>> split_bill(300, 4)          # 300 + 10% tip = 330, / 4
    82.5
    >>> split_bill(100, 3, tip_percent=0)
    33.33
    """
    total_with_tip = total * (1 + tip_percent / 100)
    per_person = total_with_tip / people
    return round(per_person, 2)


def format_student_card(name: str, age: int, gpa: float) -> str:
    """Exercise 1.5 — Build a one-line student card using an f-string.

    The GPA must always show exactly 2 decimal places.

    >>> format_student_card("Aru", 20, 3.7)
    'Name: Aru | Age: 20 | GPA: 3.70'
    """
    return f"Name: {name} | Age: {age} | GPA: {gpa:.2f}"


if __name__ == "__main__":
    # Input/output practice: run `python ex01_variables_operators.py`
    print("Worked example:", celsius_to_fahrenheit(36.6), "°F")
    name = input("Your name: ")
    age = int(input("Your age: "))          # input() always returns a str
    print(f"Hi {name}! Next year you will be {age + 1}.")
