'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import random
import os
import time

# Variable for parkings
card = ["Debit","TnG","park"]
found = False
price = 0.0
member = True
loop = 1
boolEntry = False

# ----------------------------------------------------------------------------------

#Simulate hours park
# Variable for generate a random time between 0:00 and 23:59
hours = random.randint(0, 23)  #24 hours
minutes = random.randint(0, 59) #60 minutes

# Variable for combine hours and minutes to get a random time in decimal format
hour_park = hours + minutes / 60

# print(hours)
# print(minutes)
# print(hour_park)

# ----------------------------------------------------------------------------------

# Simulate Debit/TnG Balance
debit_tng_balance = random.uniform(1.0, 100.0)

# ----------------------------------------------------------------------------------

# clear terminal function
def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

# ---------------------------------------------------------------------------------

# Function to calculate total payment 
def calculation(price):
    if hour_park <= 1:
        price = 1.0
    elif hour_park > 1 and hour_park <= 2:
        price = 1.0 + (hour_park - 1) * 1.5
    elif hour_park > 2:
        price = 1.0 + 1.5 + (hour_park - 2) * 2
    
    if member:
        price = price * 0.8
    
    return price

# ----------------------------------------------------------------------------------

def checkAMPM():
	if inAMPM.upper() == "PM" or inAMPM.upper() == "AM":
		return False;
	else:
		return True;



# ----------------------------------------------------------------------------------


while loop != -9:
    clear_terminal()
    print("Welcome to Parking Lot Payment System\n\n")

    while boolEntry == False:
        print("Entry Time in 12 hours format\n")
        inHour = input("Please enter entry Hour: ")
        inMin = input("Please enter entry Minute: ")
        inAMPM = input("Please enter AM or PM: ")
        print(inAMPM)
        if int(inHour) > 12 or int(inHour) < 0 or int(inMin) > 59 or int(inMin) < 0 or checkAMPM():
            boolEntry = False
            print("Please insert valid time!!!")
            time.sleep(2)
            clear_terminal()
        else:
            boolEntry = True
            print(f"Entry time is: {inHour}:{inMin} {inAMPM.upper()}\n")

    print(".....\n")

    print("Exit Time:\n")
    outHour = input("Please enter exit Hour: ")
    outMin = input("Please enter exit Minute")
    exit_time = int(outHour) + int(outMin) / 60
    print(f"Exit time is: {exit_time:.2f}")
