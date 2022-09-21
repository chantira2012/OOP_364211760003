"""
Student Name: Chantira Phoembun
ID: 364211760003
Grop: MIT221

"""
class student:
    def __init__(self,name,id):
        #attributes
        self.name = name #public member
        self.__id = id #private member
    def __str__(self):
        print(f'name: {self.name} id: {self.__id}')


std = student("chantira","003")
#direct access
#print(std.name,std.id)
std.__str__()

std.name = "taramart" #change data attribute
std.__str__()

std.id = "007"
std.__str__()

#name mangling
print(std._student__id)

std._student__id = "007"
std.__str__()