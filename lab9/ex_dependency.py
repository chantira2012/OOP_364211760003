"""
Student Name: Chantira Phoembun
ID: 364211760003
Grop: MIT221

"""
#class Relatione - Dependency
from datetime import date

class customer:
    def __init__(self,cusid,name):
        self.cusid = cusid
        self.name = name

    def customer_info(self):
        return f'CusID: {self.cusid} customer name: {self.name}'

class order:
    def __init__(self,orderid,date,customer,total):
        self.orderid = orderid
        self.date = date
        self.customer = customer
        self.total = total

    def order_info(self):
        print("order description:")
        print(f'\tcustomer info: {self.customer.customer_info()}')
        print(f'\tdate: {self.date}')
        print(f'\ttotal cost: {self.total}')

#create object
cus1 = customer("cus001","chantira phoembum")

order1 = order("order001",date.today(),cus1,15000)

order1.order_info()
