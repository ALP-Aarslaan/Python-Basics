class Student:
    id = " "
    cgpa = " "


jonayed = Student()
print(isinstance(jonayed, Student))

jonayed.id = "19101019"
jonayed.cgpa = 3.89

print("id : ", jonayed.id, ". cgpa : ", jonayed.cgpa)
