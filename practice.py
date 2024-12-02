# Trying to create a program that works like a simple bank account, withdrawing and depositing money

class BankAccount:
    def __init__(self, account_name, initial_balance):
        self.account_name = account_name
        self.initial_balance = initial_balance
    
    def __str__(self):
        return f'{self.account_name} has ${self.initial_balance} in their bank account!'

    def deposit(self, deposited_money):
        self.initial_balance += deposited_money
    
    def withdraw(self, withdrawn_money):
        if withdrawn_money > self.initial_balance:
            print("Insufficient Funds.")
        else:
            self.initial_balance -= withdrawn_money
            print(f'You have chosen to withdraw ${withdrawn_money} from your account. Your new balance is ${self.initial_balance}!')

    def get_balance(self):
        print(f'{self.account_name}, you have ${self.initial_balance} in your account!')      

    


# Main
my_account = BankAccount("Tyson Williams", 500)

my_account.get_balance()

my_account.withdraw(200)
my_account.withdraw(300)
my_account.withdraw(50)

