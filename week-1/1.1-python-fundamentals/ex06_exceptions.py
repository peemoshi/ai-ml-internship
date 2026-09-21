"""
Topic 6 — Exceptions (error handling)
=====================================

WHAT THIS TOPIC SOLVES
    Some problems are EXPECTED at runtime: a user types "abc" instead of a
    number, a file is missing, a config file is broken. try/except lets the
    program handle those calmly.

    GOLDEN RULE: catch the SPECIFIC exception you expect (ValueError,
    FileNotFoundError ...). A bare `except:` or `except Exception:` hides
    real bugs, and the guide explicitly warns against it.

    try:      code that might fail
    except:   what to do if a specific error happens
    else:     runs only if no error happened
    finally:  always runs (cleanup)
    raise:    signal an error yourself

WORKED EXAMPLE
"""

import json


def safe_int(text: str, default: int = 0) -> int:
    """Convert text to int, returning `default` if it isn't a valid integer.

    >>> safe_int("42")
    42
    >>> safe_int("forty-two")
    0
    """
    try:
        value = int(text)
    except ValueError:
        return default
    else:
        return value


# ---------------------------------------------------------------------------
# EXERCISES — check with:   pytest tests/test_ex06_exceptions.py -v
# ---------------------------------------------------------------------------


def safe_divide(a: float, b: float):
    """Exercise 6.1 — Return a / b, or None if b is zero.

    Only handle ZeroDivisionError. If someone passes a string, the
    TypeError must NOT be hidden — let it propagate.

    >>> safe_divide(10, 4)
    2.5
    >>> safe_divide(1, 0) is None
    True
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def parse_age(text: str) -> int:
    """Exercise 6.2 — Turn user input into a valid age.

    - Strip spaces, then convert to int.
    - If it isn't a whole number, raise ValueError("Age must be a whole number").
    - If it is outside 0–120, raise ValueError("Age must be between 0 and 120").

    >>> parse_age(" 21 ")
    21
    """
    s = text.strip()
    try:
        age = int(s)
    except ValueError:
        raise ValueError("Age must be a whole number")
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120")
    return age


class InvalidScoreError(ValueError):
    """Exercise 6.3 (part A) — a custom exception. Nothing to add here:
    inheriting from ValueError is enough. Custom exceptions make errors
    easier to recognise and catch."""


def validate_score(score) -> float:
    """Exercise 6.3 (part B) — Check a score and return it unchanged if valid.

    - If `score` is not an int or float (e.g. a str, or a bool), raise TypeError.
      Note: bool is a subclass of int in Python, so check for it explicitly.
    - If it is outside 0–100, raise InvalidScoreError.

    >>> validate_score(88.5)
    88.5
    """
    # reject bool explicitly (bool is subclass of int)
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError
    if score < 0 or score > 100:
        raise InvalidScoreError()
    return score


def ask_age(attempts: int = 3, input_func=input):
    """Exercise 6.4 — Keep asking for an age until it is valid.

    - Use input_func("Enter your age: ") to read text (the tests pass a fake
      input function so they don't need a keyboard — that's why it's a
      parameter).
    - Use parse_age(). On ValueError, print the error message and try again.
    - Return the age once valid, or None after `attempts` failed tries.
    """
    tries = 0
    while tries < attempts:
        tries += 1
        text = input_func("Enter your age: ")
        try:
            return parse_age(text)
        except ValueError as e:
            print(e)
            continue
    return None


def load_config(path: str) -> dict:
    """Exercise 6.5 — Load settings from a JSON file.

    - Missing file  -> return an empty dict {}.
    - Broken JSON   -> raise ValueError("Config file is not valid JSON")
                       (use `raise ... from error` to keep the original cause).
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        raise ValueError("Config file is not valid JSON") from e


if __name__ == "__main__":
    print(safe_int("42"), safe_int("forty-two"))
    print("You entered:", ask_age())
