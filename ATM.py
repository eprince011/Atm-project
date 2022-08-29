welcome = print("Hello, Welcome To Zadic Bank Of Africa")
print("Please insert your card")

password = 1429
money = 1000000
option = 0

def continue_exit():
    process = int(input("Continue: 1           Exit: 2     :"))
    return process 

def end_process ():
    end = "End session!! Goodbye"
    pro = "please take your card"
    return end, pro



pin = int(input("Enter your 4 digit pin : "))

if pin == password:
 

    while option != 6:

        print("please select your option below: " )
        print("1 - Check Account Balance")
        print("2 - Withdraw Cash")
        print("3 - Transfer Cash")
        print("4 - Deposit money")
        print("5 - Recharge Phone")
        print("6 - cancel")
        option = int(input("select your option: "))

        if option == 1:
            print('Balance = #', money) 
            continue_exit()

        elif option == 2:
             amount = int(input('amount to withdraw : '))
             if amount < money:
                money -= amount
                print('withdrawal Successful')
                print('the amount withdrawn = #', amount)
                print('your new balance = #', money)
                process = int(input("Continue: 1                Exit: 2     :"))
                if process == 1:
                    amount = int(input('amount to withdraw : '))
             else:
                print('Insufficent Funds')

        elif option == 3:
            input('bank name: ')
            input('account number:')
            amount = int(input('amount to transfer : '))
            if amount < money:
                money -= amount
                print("transfer successful")
                print('the amount transer = #', amount)
                print('your new balance : #',money)
                continue_exit()
                
            else:
                print('Insufficent Funds')

        elif option == 4:
            amount = int(input('amount to deposit'))
            money +=amount
            print("deposit successful")
            print('your new balance: ',money)

        elif option == 5:
            input('select network: ')
            input('phone number: ')
            amount = int(input('amount to recharge : '))
            if amount < money:
                money -= amount
                print("recharge successful")
                print('the amount recharge =#, amount')
                print('your new balance: ', money)
            else:
                print('Insufficent Funds')

        elif option ==6:
            print("End session!! Goodbye")
            print('please take your card')
        else:
            print('Invalid option')
            print('Please enter the correct options from 1 - 6')
else:
    print('Invalid PIN')        
    print("please try again later")