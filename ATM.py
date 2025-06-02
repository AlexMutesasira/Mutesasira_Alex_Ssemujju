pin ='Alex@2004'
balance=20000
while True:
    passwordInput = input("enter you pin:")
    if passwordInput == pin:
        print("Welcome to your account")
        print("withdraw")
        print("deposit")
        print("cancel")
        choice = input("enter your decision:")
        if choice == "withdraw":
             amountToWithdraw = int(input("enter the amount you wanna withdraw:"))
             if amountToWithdraw > balance:
                 print("insufficient balance")
             else:
                 balance = balance - amountToWithdraw
                 print("your balance is",balance)
                 break
             
        else:
                print("wrong password")
                