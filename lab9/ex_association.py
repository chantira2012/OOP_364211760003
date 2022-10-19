"""
Student Name: Chantira Phoembun
ID: 364211760003
Grop: MIT221

"""
#class Relation association

class student:
    #class attibute
    list_teacher = list()
    def __init__(self,name,major,project):
        self.name = name
        self.major = major
        self.project = project
    def student_info(self):
        print(f' STD Name: {self.name} Major: {self.major}')
        print(f'Working on project: {self.project}')
        print(f'Advisor list: ')
        if len(self.list_teacher) == 0:
            print("\tNO advisor.")
        else:
            for x in self.list_teacher:
                x.teacher_info()
    def add_advisor(self,teacher):
        self.list_teacher.append(teacher)

class teacher:
    list_student = list()
    def __init__(self,name):
        self.name = name
    def teacher_info(self):
        print(f'teacher name: {self.name}')
    def add_advisee(self,student):
        self.list_student.append(student)
    def advisee_info(self):
        if len(self.list_student) ==0:
            print("Have no student")
        else:
            for x in self.list_student:
                print(x.name,x.project)

s1 = student("chantira","mit","iot")
s2 = student("Aem","mit","nlt")

t1 = teacher("M")
t2 = teacher("cream")

s1.student_info()
s1.add_advisor(t1)
s1.add_advisor(t2)

s1.student_info()

t1.add_advisee(s1)
t1.add_advisee(s2)

t1.teacher_info()
t1.advisee_info()

