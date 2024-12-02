class BudgetManager:
    def __init__(self,balance,income,expenses):
        self.income = income
        self.balance = balance
        self.expenses = expenses
    
    def check_balance(self):
        return f'Your balance is ${self.balance}'

    def add_income(self):
        pass

    def add_expense(self):
        pass