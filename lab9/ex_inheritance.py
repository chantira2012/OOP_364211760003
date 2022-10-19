"""
Student Name: Chantira Phoembun
ID: 364211760003
Grop: MIT221

"""

#class Relation - inheritance

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def person_info(self):
        print(f'Name: {self.name} Age: {self.age}')

class student(person):
    def __init__(self,name,age,major,gpa):
        #1
        person.__init__(self,name,age)
        #2
        #super().__init__(name,age)
        self.major = major
        self.gpa = gpa
    def student_info(self):
        self.person_info()
        print(f'Major: {self.major} GPA: {self.gpa}')

#create object
p1 = person("chantira",21)
s1 = student("chayanin",22,"MIT",3.00)

p1.person_info()
s1.person_info()

s1.student_info()