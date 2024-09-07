print("Welcome to Python pizza Deliveries!")
size = input("What is the size of the pizza you want? S M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y OR N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill += 15
    print(f"The small size pizza is ")
elif size == "M":
    bill += 20
elif size == "L":
    bill +=25
else:
    print("You types wrong input.")

if pepperoni =="Y":
    if size == "S":
        bill += 2
    elif size == "M" or "L":
        bill += 3
else:
    bill == bill

if extra_cheese == "Y":
    bill += 1
else:
    bill == bill

print(f"Your final bill is ${bill}.")