#create a new account
Account={}
while True:
    print("1)Create account")
    print("2)Deposite money")
    print("3)Withdraw money")
    print("4)Display acc_details")
    print("5)Exit")
    option=int(input("Enter your option"))
    if option==1:
        name=str(input("Enter your name :"))
        acc_no=int(input("Enter the account number :"))
        ini_balance=int(input("Enter the initial balance :"))
        acc_data={}
        acc_data['Name']=name
        acc_data['Account number']=acc_no
        acc_data['Initial balance']=ini_balance
        Account[acc_no]=acc_data
        print("Your account created successfully")
#deposit money into the account
    elif option==2:
        acc_no=int(input("Enter the account number :"))
        if acc_no in Account:
            deposit=int(input("Enter the amount :"))
            if deposit>=0:
                Account[acc_no]['Initial balance'] += deposit
                print("Money dposited successfully.",deposit)
            else:
                print("Invalid deposit amount")
        else:
            print("Account not found")             
#withdrow money from the account
    elif option==3:
        acc_no=int(input("Enter the account number :"))
        if acc_no in Account:  
            withdraw=int(input("Enter the amount :")) 
            if withdraw>=0:
                Account[acc_no]['Initial balance']-=withdraw
                print("Money withdrawed successfully.",withdraw)
            else:
                print("Invalid amount")
        else:
            print("Account not found")  
#display account details
    elif option==4:
        acc_no=int(input("Enter the account number :"))
        if acc_no in Account:
             acc = Account[acc_no]
             print("..........ACCOUNT DETAILS..........")
             print(Account[acc_no])
        else:
            print("Account not found")
#exit from the system
    elif option==5:
        print("Exit.....")


            

        

    

        
           
