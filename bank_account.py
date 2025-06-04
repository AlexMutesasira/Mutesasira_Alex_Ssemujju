# Real world scenarios or problems
# Bank account: saving account and current account inherit from bank account

# deposit , withdraw , display balance , types of accounts

# super class

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number #create variables that store the account number
        self.balance = balance # create variables that store the 
    
    def deposit(self,amount):
        self.balance += amount # add the amount to the balance
        print(f'Deposited {amount}. New balance: {self.balance}')
    
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount # remove the amount to the balance
            print(f'Withdrawal {amount}. New balance: {self.balance}')
        else:
            print('Insufficient balance')   
    
    def display_balance(self):
        print(f'Account balance: {self.balance}')
        
# subclass : saving account

class SavingAccount(BankAccount):
    def __init__(self, account_number, balance,interest_rate ):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate # variable that stores the interest rate
        
    # Add new method for interest rate calculation
    
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        # Add the interest to the balance
        self.balance += interest
        print(f'Interest of {interest} added. New balance: {self.balance}')
        
    
    
# subclass : current account

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance,overdraft_limit ):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit # variable that stores the overdraft limit
        
       # override withdraw method to allow overdraft
       
    def withdraw(self,amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount # remove the amount to the balance
            print(f'Withdrawal {amount}. New balance: {self.balance}')
        
        else:
            print('You have exceeded the overdraft limit.')
            
# creating the objects

saving = SavingAccount('QWERTY1234', 100000, 5)
current = CurrentAccount('12345QWERTY', 5000, 10)

# test method display
saving.display_balance()
saving.add_interest()
saving.withdraw(20000)
print(' LB ...........')

current.display_balance()
current.withdraw(70000)
current.withdraw(45000)