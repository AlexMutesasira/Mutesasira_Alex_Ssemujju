# two conditions should be met
# 1. if the first condition is true
# 2. the second condition is true

age = int(input("Enter your age:"))
if age >= 18:
        print("You are an adult")
        has_ticket = input("Do you have a valid ticket ? (yes/no):")
        if has_ticket.lower() == "yes":
            print("You are allowed to enter the party")
        else:
            print("You are not allowed to enter the party")
else:
    print("You are not allowed to enter this party")