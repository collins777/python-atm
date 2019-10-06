# Name: Brandon Collins
# Date: 6/24/2018
# Description: Create a program that simulates an ATM that will perform the following functions
# Balance Inquiry, Deposit, Withdrawal, Balance Transfer from Checkings to Savings vice versa
# History of last 5 transactions

# Define Variables

deposit_amount = 0.0
withdrawal_amount = 0.0
balance_transfer = 0.0
checking_balance = 1000.00
savings_balance = 1000.00
pin_number = 0
pin_input= 0
choice = 0

# Define Constants

VALID_PIN = 1234

# Define lists

transaction_history = []



# MAIN MENU FUNCTION ----------------------------------------------------- FINISHED

def main_menu():
    #global choice

    print('''
*************************************************
*  1. Balance Inquiry\t\t\t\t*
*  2. Deposit Funds\t\t\t\t*
*  3. Withdrawal Funds\t\t\t\t*
*  4. Transfer Funds\t\t\t\t*
*  5. History of Last 5 Transactions\t\t*
*  6. Exit\t\t\t\t\t*
*************************************************
''')
    
    choice = int(input("Choice ==>"))
    
    while(choice > 6):
        print('''
*************************************************
*  1. Balance Inquiry\t\t\t\t*
*  2. Deposit Funds\t\t\t\t*
*  3. Withdrawal Funds\t\t\t\t*
*  4. Transfer Funds\t\t\t\t*
*  5. History of Last 5 Transactions\t\t*
*  6. Exit\t\t\t\t\t*
*************************************************
''')
        choice = int(input("***Invalid Entry*** Choice==>"))
        #break
    
    if(choice == 1):
        balance()
    elif(choice == 2):
        deposit()
    elif(choice == 3):
        withdrawal()
    elif(choice == 4):
        transfer()
    elif(choice == 5):
        history()
   
 



    
        


# ---------------------------------------- FUNCTIONS ---------------------------------------  

# Balance Inquiry Function ------------------------------------------------------ FINISHED

    #Display both checkings and savings amounts
    #each balance should update if the user withdrawals or deposits cash
def balance():
    print("Checking Balance: $", format(checking_balance, ',.2f'), sep="")
    print("Saving Balance: $", format(savings_balance, ',.2f'), sep="")
    transaction_history.append('Balance Inquiry')
    main_menu()







# Desposit Function --------------------------------------------------------- FINISHED

    # allow user to add to existing balance
def deposit():

    global checking_balance 
    global savings_balance
    

    print('''
*************************************************
*  1. Checking Account\t\t\t\t*
*  2. Saving Account\t\t\t\t*
*  3. Go Back To Main Menu\t\t\t*
*************************************************
''')
    choice = int(input("Choice ==>"))

    # ERROR HANDLING
    if(choice > 3):
        choice = int(input("***Invalid Entry*** Choice ==>"))
    # CHECKING ACCOUNT
    if(choice == 1):
        deposit_amount = float(input("Deposit Amount:"))
        checking_balance += deposit_amount
        # ADD VALUE TO LIST
        transaction_history.append('Deposit in Checking Account $' + str(format(deposit_amount, ',.2f'))) 
    # SAVINGS ACCOUNT
    elif(choice == 2):
        deposit_amount = float(input("Deposit Amount:"))
        savings_balance += deposit_amount
        # ADD VALUE TO LIST
        transaction_history.append('Deposit in Saving Account $' + str(format(deposit_amount, ',.2f')))

    # MAIN MENU 
    elif(choice == 3):
        main_menu()
    
    main_menu()








# Withdrawal Function -------------------------------------------------- FINISHED

    # allow user to withdrawal from exisiting balance as long as funds are available
    # withdrawals can on only be made in incriments of 10 (use modulus)
def withdrawal():

    global checking_balance
    global savings_balance

    print('''
*************************************************
*  1. Checking Account\t\t\t\t*
*  2. Saving Account\t\t\t\t*
*  3. Go Back To Main Menu\t\t\t*
*************************************************
''')
    choice = int(input("Choice ==>"))

    # ERROR HANDLING
    if(choice > 3):
        choice = int(input("***Invalid Entry*** Choice ==>"))

    # WITHDRAWAL FROM CHECKING ACCOUNT
    if(choice == 1):
        withdrawal_amount = float(input("Withdrawal Amount:"))
        
        if(withdrawal_amount % 10 == 0) and (withdrawal_amount < checking_balance):
            checking_balance -= withdrawal_amount
            # ADD VALUE TO LIST
            transaction_history.append('Withdrawal from Checking Account $' + str(format(withdrawal_amount, ',.2f'))) 
        elif(withdrawal_amount % 10 != 0):
            withdrawal_amount = float(input("Invalid Withdrawal Amount, Must be denomination of 10:"))
            checking_balance -= withdrawal_amount
        elif(withdrawal_amount % 10 == 0) and(withdrawal_amount > checking_balance):
            print("***Not Sufficent Funds in Checking Account***")
    # WITHDRAWAL FROM SAVINGS ACCOUNT     
    elif(choice == 2):
        withdrawal_amount = float(input("Withdrawal Amount:"))

        if(withdrawal_amount % 10 == 0) and (withdrawal_amount < savings_balance):
            savings_balance -= withdrawal_amount
            # ADD VALUE TO LIST
            transaction_history.append('Withdrawal from Saving Account $' + str(format(withdrawal_amount, ',.2f')))
        elif(withdrawal_amount % 10 != 0):
            withdrawal_amount = float(input("Invalid Withdrawal Amount, Must be denomination of 10:"))
            savings_balance -= withdrawal_amount
        elif(withdrawal_amount % 10 == 0) and (withdrawal_amount > savings_balance):
            print("***Not Sufficent Funds in Savings Account***")
    elif(choice == 3):
        main_menu()

    main_menu()

# Balance Transfer Function --------------------------- FINISHED

    # allow the user to transfer between accounts as long as funds are available
def transfer():

    global checking_balance
    global savings_balance


    print('''
*************************************************
*  1. Transfer to Checking Account\t\t*
*  2. Transfer to Saving Account\t\t*
*  3. Go Back To Main Menu\t\t\t*
*************************************************
''')

    choice = int(input("Choice ==>"))
    
    # ERROR HANDLING
    if(choice > 3):
        choice = int(input("***Invalid Entry*** Choice ==>"))

    # TRANSFER TO CHECKING ACCOUNT
    if(choice == 1):
        transfer_amount = float(input("Transfer Amount:"))

        if(transfer_amount <= checking_balance):
            checking_balance += transfer_amount
            savings_balance -= transfer_amount
            # ADD VALUE TO LIST
            transaction_history.append('Transfer to Checking Account $' + str(format(transfer_amount, ',.2f')))
        elif(transfer_amount > checking_balance):
            print('***Not Sufficent Funds in Checking Account***"')

    # TRANSFER TO SAVINGS ACCOUNT
    elif(choice == 2):
        transfer_amount = float(input("Transfer Amount:"))

        if(transfer_amount <= savings_balance):
            savings_balance += transfer_amount
            checking_balance -= transfer_amount
            # ADD VALUE TO LIST
            transaction_history.append('Transfer to Saving Account $' + str(format(transfer_amount, ',.2f'))) 
        elif(transfer_amount > savings_balance):
            print('***Not Sufficent Funds in Savings Account***"')
    elif(choice == 3):
        main_menu()
    
    main_menu()
    
    

# History Function------------- FINISHED 
 
def history():
    global transaction_history


    
    # makes sure list only displays last 5 transactions 
    while(len(transaction_history) > 5):
        transaction_history.pop(0)
        
    # reverse list
    transaction_history.reverse()


    print("Transaction History")
    print("--------------------")

    for num, value in enumerate(transaction_history, 1):
        print(str(num) + '.',value)
   
    print("")
    main_menu()

    # display only the last 5 transactions in chronological order



# Display Welcome Message

print("Welcome to MCC ATM")

# Ask User to Input Pin Number ------------------------------- FINISHED

pin_input = int(input("Enter your PIN:"))

for count in range(1,4):
    if(count == 3) and (pin_input != VALID_PIN):
        pin_input = int(input("Invalid PIN entered 3 times. Exiting Program."))
    elif(pin_input != VALID_PIN):
        pin_input = int(input("***Invalid PIN Entered***  Enter your PIN:"))
    elif(pin_input == VALID_PIN):
        

# CALL TO MAIN MENU FUNCTION

        main_menu()



    

 
