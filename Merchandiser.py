def merchandiser():
    dairy_items = ["Freshmilk", "NAN Gold", "Promil Gold"]
    dairy_prices = [150, 1590, 1480]

    wetgoods_items = ["Ground Beef", "Chicken Wings", "Pork Knuckles"]
    wetgoods_prices = [450, 280, 350]
    print("Welcome, You are a Merchandiser!!!.")

    print("Dairy items: ", dairy_items)
    print("Wetgoods items: ", wetgoods_items)
    print("Enter 1 to add an item.")
    print("Enter 2 to edit an item.")
    print("Enter 3 to remove an item.")
    print("Enter 4 to exit.")

    option = int(input("Enter your choice: "))

    if option == 1:
        category = input("Please enter the category of the new item (dairy or wetgoods): ")
        item = input("Enter the name of the item: ")
        price = int(input("Enter the price of the item: "))

        if category == "dairy":
            dairy_items.append(item)
            dairy_prices.append(price)
            print(dairy_items, dairy_prices)

        elif category == "wetgoods":
            wetgoods_items.append(item)
            wetgoods_prices.append(price)
            print(wetgoods_items, wetgoods_prices)
        else:
            print("Invalid")

    elif option == 2:
        category = input("Please enter the category of the item you want to edit (dairy or wetgoods): ")

        if category == "dairy":
            print(dairy_items, dairy_prices)
            edit = int(input("Enter the number of the item you want to edit: ")) - 1
            item = input("Enter the new item name: ")
            price = int(input("Enter the new item price: "))
            dairy_items[edit] = item
            dairy_prices[edit] = price
            print(dairy_items, dairy_prices)

        elif category == "wetgoods":
            print(wetgoods_items, wetgoods_prices)
            edit = int(input("Enter the number of the item you want to edit: ")) - 1
            item = input("Enter the new item name: ")
            price = int(input("Enter the new item price: "))
            wetgoods_items[edit] = item
            wetgoods_prices[edit] = price
            print(wetgoods_items, wetgoods_prices)

        else:
            print("Invalid")

    elif option == 3:
        category = input("Please enter the category of the item you want to delete (dairy or wetgoods): ")

        if category == "dairy":
            print(dairy_items, dairy_prices)
            delete = int(input("Enter the number of the item you want to delete: ")) - 1
            dairy_items.pop(delete)
            dairy_prices.pop(delete)
            print(dairy_items, dairy_prices)

        if category == "wetgoods":
            print(wetgoods_items, wetgoods_prices)
            delete = int(input("Enter the number of the item you want to delete: ")) - 1
            wetgoods_items.pop(delete)
            wetgoods_prices.pop(delete)
            print(wetgoods_items, wetgoods_prices)

    else:
        print("Invalid")