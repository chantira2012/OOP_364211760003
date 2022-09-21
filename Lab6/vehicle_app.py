from vehicle import vehicle

# display
def display_vehicle():
    if len(my_vehicle) == 0:
            print("you had no vehicle data.")
    else:
        print(f'you had {len(my_vehicle)} following:')
        for x in my_vehicle:
            x.vehicle_detail()
            print("\n")

#option
def display_option():
    select = 0
    print("welcome to vehicle data store system (VDSS)")
    print("1.add vehicle")
    print("2.display all vehicle")
    print("3.exit")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_vehicle_data()
    elif select == 2:
        display_vehicle()
    elif select == 3:
        print("Good Bye")
        exit(0)
    else:
        print("please, select number 1-3.")

#input data
def input_vehicle_data():
    brandname = input("Enter vehicle breadname: ")
    model = input("Enter vehicle model: ")
    color = input("Enter vehicle color: ")
    max_speed = int(input("Enter vehicle max_speed:"))
    price = float(input("Enter vehicle price: "))

    #return breadname,model,color,max_speen,price #return as tuple
    my_vehicle.append(vehicle(brandname,model,color,max_speed,price)) #return as tuple
    print("\n-------------------------------------------------")
    print("already add vehicle to store.")
    print("\n-------------------------------------------------")

my_vehicle = []
s = 0
while s == 0:
    display_option()


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