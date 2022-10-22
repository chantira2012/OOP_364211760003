"""
Student Name: Chantira Phoembun
ID: 364211760003
Grop: MIT221

"""
from model import Person,Student,Vaccine,Vaccine_Passport

p1 = Person("Chantira",21,74.0,156)

v1 = Vaccine("Astrazeneca")
d1 = "10/7/2564"

vp1 = Vaccine_Passport(p1)

vp1.vaccine_passport_info()

vp1.add_vaccine(v1)
vp1.add_date(d1)

vp1.vaccine_passport_info()

v2 = Vaccine("Moderna")
d2 = "10/9/2564"

vp1.add_vaccine(v2)
vp1.add_date(d2)

vp1.vaccine_passport_info()

s1 = Student("chayanin",22,78,167,"MIT")

v3 = Vaccine("Sinopharm")
d3 = "22/10/2564"

vp2 = Vaccine_Passport(s1)
vp2.add_vaccine(v3)
vp2.add_date(d3)


vp2.vaccine_passport_info()

