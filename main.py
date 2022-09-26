from Car.car import Car
from Car.Exeptions import *
car = Car()
while True:
    print("turn on , increase velocity , decrease velocity , turn lights , set Current velocity , get current velocity ......")
    choice = input("enter your choice: ")
    if choice == "turn on":
        car.turnOn()
        print("car turned on")
    elif choice == "increase velocity":
        while True:
            try:
                car.increaseVelocity()
                break
            except CarTurnedOffError as ex:
                print(ex , " turn on the car first")
            except MaxvelocityError as ex:
                print(ex)
            break
    elif choice == "decrease velocity":
        while True:
            try:
                car.decreaseVelociy()
                break
            except CarTurnedOffError as ex:
                print(ex , " turn on the car")
            except MinVelocityError as ex:
                print(ex)
            break
    elif choice == "set current velocity":
        while True



