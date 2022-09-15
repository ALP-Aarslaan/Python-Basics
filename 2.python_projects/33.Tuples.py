"""
tuples are another type of data structures in python
we can not change values of tuples after once we initializes
we can not invoke elements in another element
but we can declare tuples under tuples.
tuples are faster than lists
"""

students = (
    "Mohammad jonayed sarkar",
    "ahsan shakil",
    "ahsan asim",
    ("i am jonayed", "i am a cse student", "CGPA : 3.89")
)
print(students[0])
print(students[1:])
print(students[3:])
print(students)