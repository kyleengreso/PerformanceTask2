import Customer
import Merchandiser

userID = int(input("Enter UserID ( 0 for Merchandiser, 1 for Customer): "))
username = input("Enter Username: ")

if userID == 1:
    Customer.customerfile()

elif userID == 0:
    Merchandiser.merchandiser()

else:
    print("Invalid")
