# by epicperson04
# tested in python 3.7.6

import os # not needed in exam / psuedocode

# below lists hold all information in parralell for the devices
category_list = ["Phone","Phone","Phone","Phone","Phone","Phone","Tablet","Tablet","Tablet","Tablet","SIM card","SIM card","Case","Case","Charger","Charger"]
itemCode_list = ["BPCM","BPSH","RPSS","RPLL","YPLS","YPLL","RTMS","RTLM","YTLM","YTLL","SMNO","SMPG","CSST","CSLX","CGCR","CGHM"]
desc_list = ["Compact","Clam Shell","Robo 5,64","Robo 6,256","Y stand","Y deluxe","RTaB 8,64","RTab 10,256","YTab stand",
"YTab deluxe","no SIM","yes SIM","Standard","Luxury","Car","Home"]
price_list = [29.99,49.99,199.99,499.99,549.99,649.99,149.99,299.99,499.99,599.99,0,9.99,0,50,19.99,15.99]

money_saved = 0 # stores amount of money saved
cart = [] # this array stores all the items + accessories bought for one device
anotherDevice = True # this allows the loop to run. if this is set to false then the loop will stop running and user will not be able to buy devices
discountEnabled = False # the second time a user buys a device this is enabled which gives the 10% discount
total_cost = 0 # holds the total cost
current_deviceCost = 0

while anotherDevice is True:
    cart = [] # sets cart to 0 for each session

    device_code = input("Enter the ITEMCODE of the Phone/Tablet you want: ")
    while device_code not in itemCode_list: # checks to see if the entered device code is valid
        print("That code doesn't exist!")
        device_code = input("Enter the ITEMCODE of the Phone/Tablet you want: ")
    cart.append(device_code) # adds the valid device code to the cart array

    simCard = input("Do you want a SIM card in your phone? (y/n)")
    if simCard == "y":
        cart.append("SMPG") # adds the SIM card itemCode to the cart array
    else:
        cart.append("SMNO") # adds the no sim card itemCode to the cart array

    case = input("Do you want luxury (1) or standard (2) case?")
    if case == "1":
        cart.append("CSLX") # adds the luxury itemCode to the cart array
    else:
        cart.append("CSST") # adds the standard itemCode to the cart array

    charger = input("Would you like to buy a charger? (y/n) ")
    if charger == "y":
        charger = input("Would you like to buy the home charger (0), the car charger (1) or both (2)?")
        if charger == "0":
            cart.append("CGHM") # adds home charger itemCode to cart array
        elif charger == "1":
            cart.append("CGCR") # adds car charger itemCode to cart array
        elif charger == "2":
            cart.append("CGCR") # adds both car & home charger itemCode to cart array
            cart.append("CGHM")

    for i in range(0,16): # i takes the value from 0 to 16
        if itemCode_list[i] in cart: # check to see if any value of itemCode_list is in the cart array
            current_deviceCost =+ price_list[i] # adds the price of that item to the total cost


    if discountEnabled is True: # this means that it is the second or more device bought so a disount is added
        money_saved =+ current_deviceCost * 0.1
        current_deviceCost =+ current_deviceCost * 0.9

    print(current_deviceCost)

    another = input("Would you like to buy another device? (y/n)")
    if another == "n":
        anotherDevice = False # this means that the loop will not be repeated again so no more devices bought
    else:
        discountEnabled = True # enables the discount of 10% for the next device

    total_cost =+ current_deviceCost # adds current_deviceCost to total_cost

    current_deviceCost = 0 # resets current_deviceCost for next device (if any)

os.system('clear') # clears the screen. not needed in exam/ psuedocode
print("You need to pay", total_cost) # prints out money needed to pay
print("You saved", money_saved) # prints out money saved

# Yay!
print("\nCode written by epicperson04. Don't just copy this code and claim it as your own since that won't work in the exam. Try to rewrite this code in your own way to make sure you understand what you are writing.")
done = input("\nPress ENTER to close >>> ")
