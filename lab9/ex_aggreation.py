"""
Student Name: Chantira Phoembun
ID: 364211760003
Grop: MIT221

"""

class teacher:
    def __init__(self,name):
        self.name = name
    def teacher_info(self):
        print(f'teacher name: {self.name}')


class faculty:
    #class attributr
    list_teacher = list()

    def __init__(self,fac_name):
        self.fac_name = fac_name
    def fac_info(self):
        print(f'faculty name: {self.fac_name}')
    def add_teacher(self,teacher):
        self.list_teacher.append(teacher)
    def teacher_info(self):
        print(f'faculty {self.fac_name} has teacher following:')
        if len(self.list_teacher) ==0:
            print("No teacher.")
        else:
            for x in  self.list_teacher:
                x.teacher_info()

#create object
t1 = teacher("m")
t2 = teacher("cream")

f1 = faculty("MIT")

t1.teacher_info()
f1.fac_info()

f1.add_teacher(t1)
f1.add_teacher(t2)
f1.teacher_info()

del f1

t1.teacher_info()