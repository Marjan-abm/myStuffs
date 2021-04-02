from datetime import datetime
now = datetime.now()

account = 100
name = input('What is your name? \n')
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['passwordSeyi','passwordMike','passwordLove']
if name in allowedUsers:
    password = input("Your password? \n")
    userId = allowedUsers.index(name)
    if password == allowedPassword[userId]:
        print('Welcome %s'%name)
        print("Today's date and time is : ",now)
        print('These are the available options : ')
        print('1. withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        selectedOptions = int(input('Please select an option : '))
        if selectedOptions == 1 :
            print('You selected %s' %selectedOptions)
            withdraw = int(input("How much would you like to withdraw? "))
            print("Take your cash")
            account -= withdraw
            print("Your current balance is : %d" %account)
        elif selectedOptions == 2 :
            print('You selected %s' %selectedOptions)
            deposit = int(input("How much would you like to deposit? "))
            account += deposit
            print("Your current balance is : %d" %account)
        elif selectedOptions == 3 :
            print('You selected %s' %selectedOptions)
            issue = input("What issue will you like to report? ")
            print("Thank you for contacting us ")
        else: 
            print('Invalid option selected, please try again')
    else:
        print('Password incorrect, please try again')
else : 
    print('Name not found, please try again')