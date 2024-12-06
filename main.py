# Creating a program for a personal budget manager. 
# The program will allow users to input income and expenses with categores (ie. food, rent, entertainment)
# Output a summary of spending, income, and remaining budget
# Save user data to a file and load it automatically on startup
# Allow exporting reports as text/pdf files for offline use

from budget_manager import BudgetManager 
from transaction import Transaction

# Main
def main():
    manager = BudgetManager(0, 0, 0)
    while True:
        print("\nPlease select an option from the menu below\n")
        print("1. Check your balance.")
        print("2. Add income.")
        print("3. Add an expense.")

        choice = input("Please enter a number and press Enter.\n")

        if choice == "1":
            print(manager.check_balance())

        elif choice == "2":
            income = input(float("Amount of income: "))
            manager.add_income(income)

        elif choice == "3":
            manager.add_expense
        
        else:
            print("Your option is not valid")


main()      



