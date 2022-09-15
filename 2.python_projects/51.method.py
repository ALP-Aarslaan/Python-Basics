class Student:
    name = ""
    id = ""
    cgpa = ""

    def setValue(self, name, id, cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa

    def display(self):
        print("name :", self.name, "\n Id :", self.id, "\n CGPA:", self.cgpa)


jonayed = Student()
jonayed.setValue("jonayed", "19101019", 3.89)
jonayed.display()
