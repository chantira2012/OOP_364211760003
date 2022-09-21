from labtop import labtop

# display
def display_labtop():
    if len(my_labtop) == 0:
            print("you had no vehicle data.")
    else:
        print(f'you had {len(my_labtop)} following:')
        for x in my_labtop:
            x.display_labtop()

#option
def display_option_system():
    select = 0
    print("welcome to vehicle data store system (VDSS)")
    print("1.add vehicle")
    print("2.display all vehicle")
    print("3.exit")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_labtop_data()
    elif select == 2:
        display_labtop()
    elif select == 3:
        print("Good Bye")
        exit(0)
    else:
        print("please, select number 1-3.")

#input data
def input_labtop_data():
    brand = input("Enter vehicle bread: ")
    model = input("Enter vehicle model: ")
    cpu = input("Enter vehicle cpu: ")
    ram = int(input("Enter vehicle ram: "))
    display = input("Enter vehicle display: ")
    storage = int(input("Enter vehicle storage:"))
    price = float(input("Enter vehicle price: "))

    my_labtop.append(labtop(brand, model, cpu, ram, display, storage, price))
    print("\n-------------------------------------------------")
    print("already add vehicle to store.")
    print("\n-------------------------------------------------")

my_labtop = []
s = 0
while s == 0:
    display_option_system()

