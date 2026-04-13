class Student:
    college = "NIT Rourkela"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

    def newname(self) :
        self.name = "kumar"

s1 = Student("Vishal")
s2 = Student("Rahul")

print(s1.name)       # Instance variable
print(Student.college)  # Class variable


s1.newname();

print(s1.name)