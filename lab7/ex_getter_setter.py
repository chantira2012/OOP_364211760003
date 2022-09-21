"""
Student Name: Chantira Phoembun
ID: 364211760003
Grop: MIT221

"""

class student:
    def __init__(self,name,id):
        #attributes
        self.__name = name #public member
        self.__id = id #private member
    #getter and setter
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_id(self):
        return self.__id

    def __str__(self):
        print(f'name: {self.__name} id: {self.__id}')

s = student("cream","003")
s.__str__()

print(s.get_name())
s.set_name("aem")

print(s.get_name())

print(s.get_id())



