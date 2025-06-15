# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance (default = 0)."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount to the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the specified amount if sufficient funds are available.
        Returns True if withdrawal is successful, otherwise False.
        """
        if amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance}")
        
