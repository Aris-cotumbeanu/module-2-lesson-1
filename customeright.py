print("welcome to the ride builder!")

print("step 1 :choose your vehicle")
print("1. bike")
print("2. car")
print()

choice = int(input("Enter your choice (1 or 2): "))
print()
if choice == 1:
    print("step2: bike type")
    print("1. scooty")
    print("2. mountain bike")
    print()

    bike_choice = int(input("Enter your choice (1 or 2): "))
    print()
    if bike_choice == 1:
        print("You have chosen :scooty!")
        print(" top speed: 80km/h")
        print("best for : city rides")

    elif bike_choice == 2:
        print("You have chosen :mountain bike!")
        print(" top speed: 40km/h")
        print("best for : off-road rides")

elif choice == 2:
    print("step2: car type")
    print("1. sedan")
    print("2. suv")
    print()

    car_choice = int(input("Enter your choice (1 or 2): "))
    print()
    if car_choice == 1:
        print("You have chosen :sedan!")
        print(" top speed: 200km/h")
        print("best for : city rides")

    elif car_choice == 2:
        print("You have chosen :suv!")
        print(" top speed: 180km/h")
        print("best for : off-road rides")
else:
    print("that was no a valid choice!")
    print("please choose a valid option next time")

print("your ride is ready! enjoy your ride!")
