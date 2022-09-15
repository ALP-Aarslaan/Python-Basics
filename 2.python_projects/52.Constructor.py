class Person:
    name = ""
    phone = ""
    job = ""

    def __init__(self, name, phone, job):
        self.name = name
        self.phone = phone
        self.job = job

    def display(self):
        print("name :",self.name, "\n phone :", self.phone, "\n job:", self.job)


jonayed = Person("Mohammad jonayed Sarkar", "01861469907", "student")
jonayed.display()
