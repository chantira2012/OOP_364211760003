"""
Student Name: Chantira Phoembun
ID: 364211760003
Grop: MIT221

"""
#polymorphim with inheritance

from math import pi
class shape:
    def area(self):
        pass

class Rectangle(shape):
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def area(self):
        return self.width*self.length

class Circie(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi*(self.radius**2)

r = Rectangle(5.0,10.0)
c = Circie(7.7)

myshape = [r,c]


for x in myshape:
    print(x.area())
