days = ["Saturday", "Sunday", "Weekday"] # array to store possible types of days
dailyTotal = 0

time = int(input("What is the time? "))
while time < 8 or time >= 24: # forces user to enter a time between 0800 and 2300
    print(f"Invalid! {time} is not a valid input! Please enter a number between 0800 and 2300.")
    time = int(input("What is the time? "))

day = input("What is the day? (Saturday, Sunday or Weekday) ")
while day not in days: # forces user to enter a correct part of the week
    print(f"Invalid! {day} is not a valid input! Please choose Saturday, Sunday or Weekday.")
    day = input("What is the day? ")

# assign max hours per day
if day == "Weekday":
    maxHours = 2
elif day == "Saturday":
    maxHours = 4
elif day == "Sunday":
    maxHours = 8

hoursA = 0 #total hours for first part of day
hoursB = 0 #total hours for second part of day
price = 0
discount = 1

hoursParking = int(input("How many hours will you park? "))
finTime = hoursParking + time # current time + hoursParking gives the end time
while hoursParking > maxHours or finTime > 24: # forces user to end an amount less than the max hours on that day
    print(f"Invalid!")
    hoursParking = int(input("How many hours will you park? "))
    finTime = hoursParking + time

for i in range(time, finTime): # goes through all numbers from start time to finish time these numbers are set to 'i'
    if i < 16:
        hoursA += 1 # if 'i' is less than 16 then an hour is added for the first part of the day (hoursA)
    else:
        hoursB += 1 # if 'i' is more than 16 then an hour is added for the second part of the day (hoursB)

# m is the multiple used to multiply the hours by
if day == "Sunday":
    pricePerHour = 2
elif day == "Weekday":
    pricePerHour = 10
elif day == "Saturday":
    pricePerHour = 4

fpn = int(input("What is your FPN: "))
checkDigit = fpn%10
if (fpn//10)%11 == checkDigit:
    if time >= 16:
        discount = 0.5 # 50% discount if later than 1600
    else:
        discount = 0.1 # 10% discount if any other time

if hoursB > 0: #if there are hours in second half of day then at $2
    price += 2 # adds $2

price += hoursA * pricePerHour # adds to price the hoursA multiplied by the multiple giving total cost for first part of day
price = price * discount # multiply price by discount

print(price) # blip blop

pricePaid = int(input("Enter amount paid: "))
while pricePaid <= price:
    print("Not enough money!")
    pricePaid = input("Enter amount paid: ")

dailyTotal += pricePaid
