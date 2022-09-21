""""
Student Name: Chantira Phoembun
ID: 364211760003
Grop: MIT221
"""

class labtop:
    my_labtop = []

    def __init__(self, brand, model, cpu, ram, display, storage, price):
        self.brand = brand
        self.model = model
        self.cpu = cpu
        self.ram = ram
        self.display = display
        self.storage = storage
        self.price = price
        self.my_labtop.append(self)

    def display_labtop(self):
        print(f'brand:{self.brand} '
              f'model:{self.model} '
              f'cpu:{self.cpu} '
              f'ram:{self.ram} '
              f'display:{self.display} '
              f'storage :{self.storage} '
              f'price:{self.price}')