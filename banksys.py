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
#deposite money into the account
    elif option==2:
        acc_no=int(input("Enter the account number :"))
        if 
         deposite=int(input("Enter the amount :"))
         if deposite >= 0:
          acc_data['Initial balance'] += deposite
          print("Money dposited successfully.",deposite)
#withdrow money from the account
    elif option==3:
        acc_no=int(input("Enter the account number :"))  
        withdraw=int(input("Enter the amount :")) 
        if withdraw >= 0:
            Account['Initial balance'] -= withdraw
            print("Money withdrawed successfully.",Account) 
#display account details
    elif option==4:
        print(Account)

        

    

        
           
