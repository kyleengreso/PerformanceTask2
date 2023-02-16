def customerfile():
    dairy_items = ["Freshmilk", "NAN Gold", "Promil Gold"]
    dairy_prices = [150, 1590, 1480]

    wetgoods_items = ["Ground Beef", "Chicken Wings", "Pork Knuckles"]
    wetgoods_prices = [450, 280, 350]

    print("Welcome, Here are the available items to buy!!!: ")
    category = input("Enter the category of the item you want to purchase (dairy or wetgoods): ")
    if category == "dairy":
        print("Dairy Items: ", dairy_items, dairy_prices)
        choice = int(input("Enter the number of item you want to purchase: ")) -1
        payment = int(input("Please enter the amount of your money: "))
        change = payment - dairy_prices[choice]
        print ("Thank you for purchasing", dairy_items[choice], "your change is", change, ".")

    elif category == "wetgoods":
        print("Wetgoods Items: ", wetgoods_items, wetgoods_prices)
        choice = int(input("Enter the number of item you want to purchase: ")) -1
        payment = int(input("Please enter the amount of your money: "))
        change = payment - wetgoods_prices[choice]
        print("Thank you for purchasing", wetgoods_items[choice], "your change is", change, ".")
