# Task 1.1 — Python Fundamentals

Solved exercises covering variables, operators, conditions, loops, functions, collections,
strings, file handling, exceptions and object-oriented programming, finished with a
gradebook mini project that combines all of them.

## Structure

| File | Topic | What it practises |
|---|---|---|
| `ex01_variables_operators.py` | Variables, types, I/O, operators | `//`, `%`, rounding, f-strings, `input()` |
| `ex02_conditions_loops.py` | Conditions & loops | grade calculator, number analyzer, FizzBuzz, pattern generator, menu program |
| `ex03_functions.py` | Functions | default args, `*args`, `**kwargs`, not mutating inputs |
| `ex04_collections_strings.py` | Lists, tuples, sets, dicts, strings | student-records mini problem, word frequency |
| `ex05_file_handling.py` | Text & CSV files | read/write/append, missing files, invalid CSV rows |
| `ex06_exceptions.py` | Exceptions | specific `except`, custom exception, retry loop, `raise ... from` |
| `ex07_oop.py` | OOP | `Student`, `ExchangeStudent` (inheritance), `Course` |
| `ex08_gradebook_project.py` | **Mini project** | loads messy `data/students.csv`, validates rows, menu-driven report |
| `tests/` | Automated tests | one `pytest` file per topic |

## How to run

From this folder (with the virtual environment activated):

```bash
# run all tests
pytest -v

# run the tests for one topic
pytest tests/test_ex02_conditions_loops.py -v

# run a program
python ex02_conditions_loops.py        # interactive menu
python ex08_gradebook_project.py       # gradebook mini project
```

## Why a class makes sense here (Topic 7)

<!-- TODO: write 2–3 sentences in your own words. -->

## Test results

<!-- TODO: paste a screenshot of `pytest -v` with everything passing. -->

## What I learned

<!-- TODO: 3–5 bullet points in your own words — e.g. a bug you hit and how you fixed it. -->
