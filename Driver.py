from Db import DbRunner
from ViewClasses import Admin, Customer, Dish, Order
import os

# Defaul class to drive the program
class Restaurant_MS:

    #=========================================================================
    # constructor to initialize the database class
    #=========================================================================
    def __init__(self,host,user,password,database):
        self.model = DbRunner(host,user,password,database)



    #=========================================================================
    # Main manu functionality 
    #=========================================================================
    def MainMenu(self):
        number = ""
        while( number != "q"):
            self.clearScreen()
            print("----------------")
            print("=  HOME__PAGE  =")
            print("----------------")
            print("1. Press 1 for Admin:")
            print("2. Press 2 for customer")
            print("q. Quit")
            number = (input())
            if( number == "1"):
                number1 = ""
                print("\n1. Admin Sign Up")
                print("2. Admin Sign In")
                number1 =  (input())
                if( number1 == "1"):
                    self.AdminSignUp()
                elif( number1 == "2"):
                    self.AdminSignIn()                    
                else:
                    print("Invalid Input")
                    input("\nPress Enter to continue...")
            elif( number == "2"):
                number1 = ""
                print("\n1. Customer Sign Up")
                print("2. Customer Sign In")
                number1 =  (input())
                if( number1 == "1"):
                    self.CustomerSignUp()
                elif( number1 == "2"):
                    self.customerLogIn()                    
                else:
                    print("Invalid Input")
            elif( number == "q"):
                print("\n----------------")
                print("see you soon !!!")
                print("----------------\n")
                exit(0)
            else:
                print("Invalid Selection")
                input("\nPress Enter to continue...") 

        input("\nPress Enter to continue...")


    #=========================================================================
    # to impliment the functionality of Admin Sign UP
    #=========================================================================
    def AdminSignUp(self):
        self.clearScreen()
        print("---------------------")
        print("|      ADMIN        |")
        print("|     SIGN UP       |")
        print("---------------------")
        name =  input("Enter Name: ")
        email =  input("Enter Email: ")
        pwd   =  input("Enter Password: ")
        while "@" not in email:
            email = input("Please enter a valid email \n")
        
        while len(pwd) < 4:
            pwd = input("Please enter a valid password \n")

        a = Admin(name, pwd, email)
        exist = self.model.checkAlreadyExist(a)
        if exist == False:
            insert = self.model.signupAdmin(a)
            if insert == True:
                print("\nYou successfully Registered")
            else:
                print("\nSignup failed")
        else:
            print("\nSorry, this admin is already exits")

        input("\nPress anything to continue...")



    #=========================================================================
    # to impliment the functionality of Admin Sign IN
    #=========================================================================
    def AdminSignIn(self):
        self.clearScreen()
        print("---------------------")
        print("|      ADMIN        |")
        print("|     SIGN IN       |")
        print("---------------------")

        email = input("Enter Email: ")
        pwd   = input("Enter Password: ")

        a = Admin("NULL", pwd,email)

        ls = self.model.signInAdmin(a)
        if len(ls) >0:
            admininp = ""
            while admininp != "q":
                self.clearScreen()
                print("---------------------")
                print("  !!! ADMIN HOME !!!")
                print("---------------------")
                print("1. to view MENU")
                print("2. to add a dish in MENU")
                print("q. to LOGOUT and back to MENU\n")
                    
                admininp = input("Select an option: ")
                if admininp == "1":
                    self.showDish()
                elif admininp == "2":
                    self.addDish()
                elif admininp == "q":
                    print("\nLogging out ....\n")
                    input("\nPress Enter to continue...")
                    break
                else:
                    print("\nOpss!!! Invalid Input, try again")
                    input("\nPress Enter to continue...")
        else:
            input("\nPress Enter to continue... ")
            

    #=========================================================================
    # to add dish in the database by getting values from user
    #=========================================================================
    def addDish(self):
        print("Please provide necessary details about Dish\n")
        name = input("Enter Name: ")
        price = input("Enter price in $: ")
        while price.isnumeric == False or int(price) < 0:
            price = input("Please enter a valid price: ")

        gr1 = input("Enter first ingredient: ")
        gr2 = input("Enter second ingredient: ")
        gr3 = input("Enter third ingredient: ")
        catg = input("Enter catagory: ")
        g_ls = [gr1, gr2, gr3]
        mydish = Dish(name, g_ls, price, catg)
        result = self.model.addDish(mydish)
        if result:
            print("=== Dish has been added in the database ===")
        else:
            print("=== ERROR! adding dish in the database ===")

        input("Press anything to continue...")



    #=========================================================================
    # To show all the dishes with details in the resturent
    #=========================================================================
    def showDish(self):
        
        data = self.model.getDishList()
        for i in range(len(data)):
            print("------------------------------------------------------")
            print(f"Dish: {i+1}")
            print(f"\tName:        {data[i][0]}")
            print(f"\tCategory:    {data[i][2]}")
            print(f"\tIngredients: {data[i][3]}, {data[i][4]}, {data[i][5]}")
            print(f"\tPrice:       {data[i][1]} $")
            
        print("------------------------------------------------------")
        input("Press Enter to continue...\n")
        return data
    
    

    #=========================================================================
    # clears console and display main header
    #=========================================================================
    def clearScreen(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  
            command = 'cls'
        os.system(command)
        print("|======================================|")
        print("|     RESTAURANT MANAGEMENT SYSTEM     |")
        print("|======================================|\n")



    #=========================================================================
    # to impliment the functionality of Customer Sign UP
    #=========================================================================
    def CustomerSignUp(self):
        self.clearScreen()
        print("---------------------")
        print("|    Customer       |")
        print("|     SIGN UP       |")
        print("---------------------")
        name =  input("Enter Name: ")
        email =  input("Enter Email: ")
        pwd   =  input("Enter Password: ")
        while "@" not in email:
            email = input("Please enter a valid email \n")
        
        while len(pwd) < 4:
            pwd = input("Please enter a valid password \n")

        a = Customer(name, pwd, email)
        exist = self.model.checkCustomerAlreadyExist(a)
        if exist == False:
            insert = self.model.signupCustomer(a)
            if insert == True:
                print("\nRespected Customer! You successfully Registered")
            else:
                print("\nSignup failed")
        else:
            print("\nSorry, this Customer is already exits")

        input("\nPress anything to continue...")




    #=========================================================================
    # to impliment the functionality of Customer Sign IN
    #=========================================================================
    def customerLogIn(self):
        print("---------------------")
        print("|     Customer      |")
        print("|     SIGN IN       |")
        print("---------------------")

        email = input("Enter Email: ")
        pwd   = input("Enter Password: ")

        a = Customer("NULL", pwd,email)

        ls = self.model.signInCustomer(a)
        if len(ls) >0:
            self.clearScreen()
            print("---------------------")
            print("!!! Customer HOME !!!")
            print("---------------------")

            print("Following dishes are available \n")
            dishes = self.showDish()
            
            myorder = []

            admininp = ""
            while admininp != "q":
                self.clearScreen()
                print("---------------------")
                print("!!! Customer HOME !!!")
                print("---------------------")
                print("1. to Add dish to the order")
                print("2. to remove dish from order")
                print("3. to view your current order")
                print("4. to Generate bill\n")
                print("H. to Show previous Orders (history)")
                print("q. to LOG OUT and Exit\n")                    
                admininp = input("Select an option: ")
                if admininp == "1":
                    for i in range(len(dishes)):
                        print(f"{i+1}. {dishes[i][3]}")
                    index = input(f"\nSelect with dish you want to add (1 to {len(dishes)}): ")
                    while index.isdigit() == False or int(index) < 1 or int(index) > len(dishes):
                        index = input(f"Please enter a valid number (1 to {len(dishes)}): ")
                        
                    
                    num = input("Enter quantity you want to buy: ")
                    while num.isdigit() == False or int(num) < 1 :
                        num = input(f"Please enter a valid number: ")

                    index = int(index)
                    indg = [dishes[index-1][3],dishes[index-1][4], dishes[index-1][5]]
                    dis = Dish(dishes[index-1][0], indg , dishes[index-1][1] ,dishes[index -1][2])
                    dis.quantity = num
                    myorder.append(dis)
                    input("\n=== Item Added ===\n\nPress Enter to continue ...")

                elif admininp == "2":
                    for i in range(len(myorder)):
                        print(f"{i+1}. {myorder[i].name}  {myorder[i].quantity} {myorder[i].price}/-")
                    index = input(f"\nSelect with dish you want to remove (1 to {len(myorder)}): ")
                    while index.isdigit() == False or int(index) < 1 or int(index) > len(myorder):
                        index = input(f"Please enter a valid number (1 to {len(myorder)}): ")
                        
                    index = int(index)
                    myorder.pop(index-1)
                    input("\n=== Item Removed ===\n\nPress Enter to continue ...")


                elif admininp == "3":
                    self.showCustomerOrder(myorder)
                elif admininp == "4":
                    if len(myorder) > 0:
                        self.CalculateResult(myorder, email)
                    else:
                        print("Opss!!! Can't generate bill, Order List is Empty \n")
                        input("\nPress Enter to continue ...")
                elif admininp == "H":
                    self.showPreviousOrder(email)
                elif admininp == "q":
                    print("\nLogging out ....\n")
                    input("\nPress Enter to continue...")
                    break
                else:
                    print("Opss!!! Invalid Input, try again \n")
                    input("\nPress Enter to continue ...")
        else:
            input("\nPress Enter to continue... ")


                    

    #=========================================================================
    # To show the details of current order of the customer
    #=========================================================================
    def showCustomerOrder(self, myorder):
        self.clearScreen()
        print("---------------------")
        print("!!! Customer HOME !!!")
        print("---------------------")

        print("Your order is: ")
        print("---------------------------------------------------------------")
        print("Sr.No  Dish\tQuantity\tPrice")
        for i in range(len(myorder)):
            print(f"{i+1}-     {myorder[i].name}\t {myorder[i].quantity} \t\t {myorder[i].price}/-")
        print("---------------------------------------------------------------")
        input("Press anything to continue ...")



    #=========================================================================
    # Function to generate the bill
    #=========================================================================
    def CalculateResult(self, myorder, email):

        dine = "dine"
        print("\n= ORDER TYPE =")
        print("1. Dining ")
        print("2. Parcel ")
        num3 = input()
        while num3 != "1" and num3 != "2":
            num3 = input("Please enter a valid input (1 or 2)")

        if num3 == "2":
            dine = "parcel"

        payment = "Credit_Card"
        print("\n= Enter payment method =")
        print("1. Credit Card ")
        print("2. Cash")
        num3 = input()
        while num3 != "1" and num3 != "2":
            num3 = input("Please enter a valid input (1 or 2)")
        if num3 == "2":
            payment = "Cash"
        sum = 0
        self.clearScreen()

        print("---------------------")
        print("!!! Customer HOME !!!")
        print("---------------------")

        print("                               BILL                    " )
        print("---------------------------------------------------------------")
        print("Sr.No  Dish\tQuantity\tPrice")
        for i in range(len(myorder)):
            print(f"{i+1}-     {myorder[i].name}\t {myorder[i].quantity} \t\t {myorder[i].price}/-")
            sum = sum + (int(myorder[i].quantity) * int(myorder[i].price))

        tax = 0.0
        if dine == "dine":
            tax = sum * .01
        gst = 0.0
        if payment == "Credit_Card":
            gst = .08 * sum
        elif payment == "Cash":
            gst = .16 * sum

        tax = round(tax, 2)
        gst = round(gst, 2)
        gtotal = sum + tax + gst

        gtotal = round(gtotal, 2)

        print(f"\nTotal        {sum} $")
        print(f"Inc. Tax     {tax} $ => ({dine})")
        print(f"GST          {gst} $ => ({payment})")
        print(f"\nGrand Total  {gtotal} $ ")
        print("---------------------------------------------------------------")
        
        ls = []
        for i in range(len(myorder)):
            order = Order(email, myorder[i].name, myorder[i].quantity, myorder[i].price)
            ls.append(order)
        
        check = self.model.storeOrder(ls, dine, payment)
        if check != True:
            print("Error! Storing in Database\n")

        input("Press anything to continue ...")


    #=========================================================================
    # To show the history of the given customer
    #=========================================================================
    def showPreviousOrder(self, email):
        orders = self.model.getOrderLists(email)
        num = 0
        self.clearScreen()
        print("                       PREVIOUS BILLS                    " )
        for order in orders:
            num = num + 1
            print(f"<= ORDER {num} =>")
            lis = self.model.getOrderData(order[0])
            lis = list(lis)
            sum = 0
            print("---------------------------------------------------------------")       
            print("Sr.No  Dish\tQuantity\tPrice")
            for i in range(len(lis)):
                print(f"{i+1}-     {lis[i][2]}\t {lis[i][4]} \t\t {lis[i][3]}/-")
                sum = sum + (int(lis[i][4]) * int(lis[i][3]))

            tax = 0.0
            dine = order[2]
            if dine == "dine":
                tax = sum * .01
            gst = 0.0
            payment = order[3]
            if payment == "Credit_Card":
                gst = .08 * sum
            elif payment == "Cash":
                gst = .16 * sum

            tax = round(tax, 2)
            gst = round(gst, 2)
            gtotal = sum + tax + gst

            gtotal = round(gtotal, 2)

            print(f"\nTotal        {sum} $")
            print(f"Inc. Tax     {tax} $ => ({dine})")
            print(f"GST          {gst} $ => ({payment})")
            print(f"\nGrand Total  {gtotal} $ ")
            print("---------------------------------------------------------------")

        input("Press Enter to continue ...")




#=========================================================================
# main function                    
#=========================================================================
def main():
    obj = Restaurant_MS("localhost","root","","rms")
    obj.MainMenu()


if __name__ == "__main__":
    main()
