print("Welcome to the Roller Coaster!!!")
height = int(input("What is the height in cm?"))
if height >= 120 :
    print("can ride")
else :
    print("can't ride")



print("Welcome to the Roller Coaster!!!")
height = int(input("What is the height in cm?"))
age = int(input("what is the age?"))
if height >= 120:
    print("you can ride")
    if age <= 18:
        print("the cost of the roller coaster ride is $7")
    else :
        print("the cost of the roller coaster is &18")
else :
    print("you can't ride the roller coaster")


print("Welcome to the Roller Coaster!!!")
height = int(input("What is the height in cm?"))
age = int(input("what is the age?"))
if height >= 120:
    print("you can ride")
    if age <= 12:
        print("the cost of the roller coaster ride is $7")
    elif age <=18:
        print("the cost of the roller coaster is $15")
    else:
        print("the cost of the roller coaster is $21")
else :
    print("you can't ride the roller coaster")


print("Welcome to the Roller Coaster!!!")
height = int(input("What is the height in cm?"))
age = int(input("what is the age?"))
bill = 0
if height >= 120:
    print("you can ride")
    if age <= 12:
        bill = 7
        print("child tickets are $7")
    elif age <=18:
        bill = 15
        print("Youth ticket is $15")
    else:
        bill = 21
        print("Adult ticket are $21")
    wants_photo=input(" do you want to have a photo take? type y for yes and n for no.")
    if wants_photo == y:
        #add $3 to their bill
        bill = bill + 3 # bill+=3
    else:
        bill == bill
    print(f"the final bill is {bill}")
else :
    print("you can't ride the roller coaster")