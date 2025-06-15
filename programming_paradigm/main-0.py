# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Extract command and amount if provided
    command_data = sys.argv[1].split(':')
    command = command_data[0]
    amount = float(command_data[1]) if len(command_data) > 1 else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
        account.display_balance()

    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
        account.display_balance()

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
    
