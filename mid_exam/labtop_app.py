from labtop import labtop

# display
def display_labtop():
    if len(my_labtop) == 0:
            print("you had no vehicle data.")
    else:
        num = 1
        print(f'you had {len(my_labtop)} following:')
        for x in my_labtop:
            print(F'{num}. ',end="")
            x.display_labtop()
            num +=1
        print("\n")

#option
def display_option_system():
    select = 0
    print("welcome to vehicle data store system (VDSS)")
    print("1.add vehicle")
    print("2.display all vehicle")
    print("3.delete laptop")
    print("4.edit labtop_price")
    print("5.exit")
    select = int(input("select(1-5)? : "))
    if select == 1:
        input_labtop_data()
    elif select == 2:
        display_labtop()
    elif select == 3:
        delete_labtop()
    elif select == 4:
        edit_labtop_price()
    elif select == 5:
        print("Good Bye")
        exit(0)
    else:
        print("please, select number 1-3.")

def edit_labtop_price():
    print("which one do you want to edit price?: ")
    display_labtop()
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select(1-{n}) or type 0 to main option:? "))
        if s in range(1, n + 1):
            print(f'old price: {my_labtop[s-1].get_price()}')
            newprice = float(input("enter nem price: "))
            my_labtop[s-1].set_price(newprice)
            print("\nlabtop price update.\n")
            break
        elif s == 0:
            break
        else:
            print(f"please, select number 1-{n} or type 0 to main options.")

#delete data
def delete_labtop():
    print("which one do you want to remove?: ")
    display_labtop()
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select(1-{n}) or type 0 to main option:? "))
        if s in range(1,n+1):
            my_labtop.pop(s-1)
            print("\nalready delete laptop data.\n")
            break
        elif s ==0:
            break
        else:
            print(f"please, select number 1-{n} or type 0 to main options.")

#input data
def input_labtop_data():
    brand = input("Enter vehicle bread: ")
    model = input("Enter vehicle model: ")
    cpu = input("Enter vehicle cpu: ")
    ram = int(input("Enter vehicle ram: "))
    display = input("Enter vehicle display: ")
    storage = int(input("Enter vehicle storage:"))
    price = float(input("Enter vehicle price: "))

    l = labtop("","","",0,0,0,0,)

    l.set_brand(brand)
    l.set_model(model)
    l.set_cpu(cpu)
    l.set_ram(ram)
    l.set_display(display)
    l.set_storage(storage)
    l.set_price(price)

    my_labtop.append(l)
    #my_labtop.append(labtop(brand, model, cpu, ram, display, storage, price))
    print("\n-------------------------------------------------")
    print("already add vehicle to store.")
    print("\n-------------------------------------------------")

my_labtop = []
my_labtop.append(labtop("asus","vivo","inter","8","15.6","512","27900"))
my_labtop.append(labtop("lenovo","ideapad","intercore","8","15.6","512","25900"))
my_labtop.append(labtop("acer","swift3","intercorei7","8","14","512","33990"))
s = 0
while s == 0:
    display_option_system()

