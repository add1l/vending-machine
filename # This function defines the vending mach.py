
def vend():

    # Define the items available in the vending machine
    w = {"item": "water", "rate": 10, "available stock": 30}
    x = {"item": "juice", "rate": 7,"available stock": 18}
    y = {"item": "tea", "rate": 2.50, "available stock": 20}
    z = {"item": "chips", "rate": 2, "available stock": 70}
    d = {"item": "cholate", "rate": 3, "available stock": 10}
    I = {"item": "chewgum", "rate": 1.50, "available stock": 40}
    o = {"item": "pepsi", "rate": 4, "available stock": 25}
    items = [w, x, y, z, d, I ,o]  # Add all items to a list

    cim = 0  # Initialize cash in machine to 0
    print ("How can I help you! \n--------------------")  # Print welcome message

    # Define a function to show items and prices
    def show(items):
        print("\nitems available \n---------------------")  # Print items available header

        # Loop through each item in the list and print its name and price
        for item in items:
            print(item.get("item") + ": £" + str(item.get("rate")))

    # Have user choose an item
    while True:  # Loop until user chooses a valid item
        show(items)  # Show items and prices
        selected_item = input("select iteam: ")  # Get user input for selected item

        # Check if selected item is valid
        for item in items:
            if selected_item == item.get("item"):  # If selected item is valid
                rate = item.get("rate")  # Get rate of selected item

                # Check if user has enough money to purchase the item
                while cim < rate:  # Loop until user has enough money
                    try:
                        cim += float(input("insert amount " + str(rate - cim) +": "))  # Add user input to cash in machine
                    except ValueError:  # If user input is not a valid number
                        print ("Please enter a valid amount.")  # Print error message
                        continue  # Continue to next iteration of while loop

                # If user has enough money, dispense the item and update cash in machine and item stock
                print("availed items " + item.get("item"))  # Print message that item has been dispensed
                item["available stock"] -= 1  # Decrease item stock by 1
                cim -= rate  # Subtract item price from cash in machine
                print ("cash remaining: " + str(cim))  # Print remaining cash in machine

                # Ask user if they want to purchase another item
                a = input("would u like something else ? (yes/no): ")  # Get user input for purchasing another item
                if a == "n":  # If user does not want to purchase another item
                    if cim != 0:  # If there is remaining cash in machine
                        print (str(cim) + " refunded")  # Print refund message
                    cim = 0  # Set cash in machine to 0
                    print ("Enjoy your drink! \n")  # Print goodbye message
                    return  # Exit both loops
                else:
                    print("Enjoy your drink! \n")  # Print goodbye message
                    return  # Exit both loops
            else:
                continue  # Continue to next iteration of for loop
        else:
            continue  # Continue to next iteration of while loop

# Call the vend function to start the vending machine program
vend()