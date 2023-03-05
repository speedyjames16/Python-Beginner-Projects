#Banking Application That Does Withdrawals, Deposits, and Balance Displays.

#Option Menu using print_menu function
def print_menu():
    print(      "Welcome to American Banking")
    print("")
    print("What would you like to do today?")
    print("1. Withdraw Funds")
    print("2. Deposit Funds")
    print("3. Check Balance")
    print("4. Exit\n")
print_menu()

#defining funds as a minimum of 50 USD
funds = 50

#creating a banking_menu function
def banking_menu():
    banking = input("Pick a number \n> ")
    funds = 50

    if banking == "1":
        withdrawal_amount = eval(input("Enter amount in dollars you'd like to withdraw "))
        if withdrawal_amount <= funds:
            funds -= withdrawal_amount
            print("Your money is printing, your new balance is " + str(funds)+ " Dollars\n")
            print("Returning to main menu...")
            

        else:
            print("Not enough balance, Try again")
            

    if banking == "2":
        deposit_amount = eval(input("Enter amount in dollars you'll be depositing "))
        print(deposit_amount)
        funds += deposit_amount
        print("Thanks for your deposit, your new balnce is " +str(funds) + " Dollars")
        
    if banking == "3":
        print ("Your balance is $" + str(funds) + " dollars\n")
        print ("Thank you, Have a Great Day")
        quit()
    
    if banking =="4":
        print ("Leaving American Banking")
        quit()

banking_menu()
print_menu()
banking_menu()
quit()
        
    

    
