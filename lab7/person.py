"""
Student Name: Chantira Phoembun
ID: 364211760003
Grop: MIT221

"""
class person:
    def __init__(self,name,age):
        self._name = name #protectd mamber
        self._age = age #protected mamber
    def __str__(self):
        print(f'name :{self._name} age:{self._age}')

class student(person):
    def __init__(self,name,age,major):
        self.major = major
        person.__init__(self,name,age)
    def __str__(self):
        print(f'name: {self._name} age: {self._age} major: {self.major}')

#object preson
p = person("chantira",20)
p.__str__()

p._name = ("tara",21)
p.__str__()

#object student
s = student("tara",22,"mit")
s.__str__()

s._name = "pronprasert"
s.__str__()