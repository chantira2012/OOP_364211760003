from vehicle import vehicle
#option
def display_option
    select = 0
    print("welcom to vehicle data store system (VDSS)")
    print("1.add vehicle")
    print("2.display all vehicle")
    print("3.exit")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_vehicle_data()
    elif select == 2:
        pass
    elif select == 3:
        exit(0)
    elif:
        print("please, select number 1-3.")

#input data
def input_vehicle_data():
    brandname = input("Enter vehicle breadname: ")
    model = input("Enter vehicle model: ")
    color = input("Enter vehicle color: ")
    max_speed = int(input("Enter vehicle max_speed:"))
    price = float(input("Enter vehicle price: "))

    #return breadname,model,color,max_speen,price #return as tuple
    return brandname,model,color,max_speed,price #return as tuple

my_vehicle = []


#vm=input_vehicle_data()
#print(vm)
#print(type(vm))

#create object of vehicle class
#v1 = vehicle(vm[0],vm[1],vm[2],vm[3],vm[4])
#display all object attributes
#v1.vehicle_detail()

#vm=input_vehicle_data()

#create object of vehicle class
#v2 = vehicle(vm[0],vm[1],vm[2],vm[3],vm[4])
#display all object attributes
#v2.vehicle_detail()