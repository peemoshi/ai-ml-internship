"""
Topic 7 — Object-oriented programming (OOP) basics
==================================================

WHAT THIS TOPIC SOLVES
    A class bundles DATA (attributes) with the BEHAVIOUR that uses it
    (methods). Instead of passing a loose dict of scores around and hoping
    every function validates it, a Student object guarantees its own rules
    (e.g. "a score is always 0–100").

    Key ideas: __init__, self, attributes, methods, __str__ / __len__,
    inheritance and super().

    WRITE IN THE README (the guide asks for this): in 2–3 sentences, why does
    using a class make sense for students and courses?

WORKED EXAMPLE
"""


class Book:
    """A library book that can be borrowed and returned."""

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self) -> bool:
        """Borrow the book. Returns False if it is already borrowed."""
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True

    def __str__(self) -> str:
        status = "borrowed" if self.is_borrowed else "available"
        return f"{self.title} by {self.author} ({status})"


# ---------------------------------------------------------------------------
# EXERCISES — check with:   pytest tests/test_ex07_oop.py -v
# ---------------------------------------------------------------------------


class Student:
    """Exercise 7.1 — A student with scores per course.

    Attributes:
        name (str), student_id (str), scores (dict: course -> score, starts empty)
    """

    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.scores = {}

    def add_score(self, course: str, score: float) -> None:
        """Store a score for a course (overwrites an existing one).
        Raise ValueError if the score is outside 0–100."""
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.scores[course] = score

    def average(self) -> float:
        """Average of all scores, rounded to 2 decimals. 0.0 if there are none."""
        if not self.scores:
            return 0.0
        avg = sum(self.scores.values()) / len(self.scores)
        return round(avg, 2)

    def __str__(self) -> str:
        """Format: 'Aru (S001) - avg 88.50'  (always 2 decimals)."""
        return f"{self.name} ({self.student_id}) - avg {self.average():.2f}"


class ExchangeStudent(Student):
    """Exercise 7.2 — Inheritance.

    Same as Student, plus a `home_university` attribute.
    Use super().__init__(...) instead of repeating code.
    __str__ adds ' [exchange: <home_university>]' to the normal Student text.
    """

    def __init__(self, name: str, student_id: str, home_university: str):
        super().__init__(name, student_id)
        self.home_university = home_university

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} [exchange: {self.home_university}]"


class Course:
    """Exercise 7.3 — A course with limited seats.

    Attributes: code (str), capacity (int), students (list of Student)
    """

    def __init__(self, code: str, capacity: int):
        self.code = code
        self.capacity = capacity
        self.students = []

    def enroll(self, student: Student) -> bool:
        """Add a student. Return False (and don't add) if the course is full
        or a student with the same student_id is already enrolled."""
        if len(self.students) >= self.capacity:
            return False
        for s in self.students:
            if s.student_id == student.student_id:
                return False
        self.students.append(student)
        return True

    def roster(self) -> list:
        """Alphabetically sorted list of enrolled students' names."""
        names = [s.name for s in self.students]
        return sorted(names)

    def __len__(self) -> int:
        """len(course) returns the number of enrolled students."""
        return len(self.students)


if __name__ == "__main__":
    book = Book("Deep Learning", "Goodfellow et al.")
    print(book)
    book.borrow()
    print(book)
