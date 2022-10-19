"""
Student Name: Chantira Phoembun
ID: 364211760003
Grop: MIT221

"""
#class Relation - composition

class faculty:
    def __init__(self,fac_name):
        self.fac_name = fac_name
    def fac_info(self):
        print(f'faculty name: {self.fac_name}')

class university:
    list_faculty = list()
    def __init__(self,uniname):
        self.uniname = uniname
        self.get_faculty()
    def uni_info(self):
        print(f'university name: {self.uniname}')
        print(f'has faculty below: ')
        if len(self.list_faculty) ==0:
            print(f'Has no faculty.')
        else:
            for x in self.list_faculty:
                x.fac_info()

    def get_faculty(self):
        f1 = faculty("MIT")
        f2 = faculty("sci-tech")
        self.list_faculty.append(f1)
        self.list_faculty.append(f2)

u1 = university("RUTS")

u1.uni_info()

u1.list_faculty[0].fac_info()