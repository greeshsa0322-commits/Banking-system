import sys
import time

class Bank:
    def __init__(self):
        self.accounts = {}             # Stores all accounts
        self.next_acc_number = 1    # Auto-generated account numbers

    def create_account(self):
        print("\n--- Create New Account ---")
        name = input("Enter Name: ")
        try:
            initial_deposit = float(input("Enter Initial Deposit: "))
        except ValueError:
            print("Invalid amount! Account not created.")
            return

        acc_num = self.next_acc_number
        self.accounts[acc_num] = {
            "name": name,
            "balance": initial_deposit
        }
        self.next_acc_number += 1

        print(f"Account Number {acc_num} created successfully!")

    def deposit(self):
        print("\n--- Deposit Money ---")
        try:
            acc_num = int(input("Enter Account Number: "))
        except ValueError:
            print("Invalid Account Number!")
            return

        if acc_num in self.accounts:
            try:
                amount = float(input("Enter Deposit Amount: "))
            except ValueError:
                print("Invalid amount!")
                return

            self.accounts[acc_num]["balance"] += amount
            print(f"Deposit successful! New balance: {self.accounts[acc_num]['balance']}")
        else:
            print("Account not found!")

    def withdraw(self):
        print("\n--- Withdraw Money ---")
        try:
            acc_num = int(input("Enter Account Number: "))
        except ValueError:
            print("Invalid Account Number!")
            return

        if acc_num in self.accounts:
            try:
                amount = float(input("Enter Withdrawal Amount: "))
            except ValueError:
                print("Invalid amount!")
                return

            if self.accounts[acc_num]["balance"] >= amount:
                self.accounts[acc_num]["balance"] -= amount
                print(f"Withdrawal successful! Remaining balance: {self.accounts[acc_num]['balance']}")
            else:
                print("Insufficient balance!")
        else:
            print("Account not found!")

    def check_balance(self):
        print("\n--- Check Balance ---")
        try:
            acc_num = int(input("Enter Account Number: "))
        except ValueError:
            print("Invalid Account Number!")
            return

        if acc_num in self.accounts:
            name = self.accounts[acc_num]["name"]
            balance = self.accounts[acc_num]["balance"]
            print(f"Account Holder: {name}")
            print(f"Current Balance: {balance}")
        else:
            print("Account not found!")

    def display_all_accounts(self):
        print("\n--- All Accounts ---")
        if not self.accounts:
            print("No accounts available.")
            return

        print(f"{'Account No.':<15}{'Name':<20}{'Balance'}")
        print("-" * 45)
        for acc, details in self.accounts.items():
            print(f"{acc:<15}{details['name']:<20}{details['balance']}")
        print("-" * 45)


def main():
    bank = Bank()

    while True:
        print("\n====== Welcome to the Bank ======")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Display All Accounts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.deposit()
        elif choice == "3":
            bank.withdraw()
        elif choice == "4":
            bank.check_balance()
        elif choice == "5":
            bank.display_all_accounts()
        elif choice == "6":
            print("Exiting the system...")
            time.sleep(1)
            sys.exit()
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
