"""
Student Name: Chantira Phoembun
ID: 364211760003
Grop: MIT221

"""
class vehicle:
    #class attribute
    my_vihecle= []

    def __init__(self,brandname,model,color,max_speed,price):
        self.brandname = brandname
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.price = price
        self.my_vihecle.append(self)

    def vehicle_detail(self):
        print(f'brandname:{self.brandname} '
              f'model:{self.model} '
              f'color:{self.color} '
              f'max_speed :{self.max_speed} '
              f'price:{self.price}')