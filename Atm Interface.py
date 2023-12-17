class ATM:
    def __init__(self, user_id, pin, balance=0, transaction_history=[]):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = transaction_history

    def authenticate_user(self):
        entered_user_id = input("Enter User ID: ")
        entered_pin = input("Enter PIN: ")

        if entered_user_id == self.user_id and entered_pin == self.pin:
            return True
        else:
            print("Invalid User ID or PIN. Access denied.")
            return False

    def display_menu(self):
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Quit")

    def check_balance(self):
        print(f"Your balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal canceled.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")

    def transfer(self, amount, recipient):
        if amount > self.balance:
            print("Insufficient funds. Transfer canceled.")
        else:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transfer to {recipient}: -${amount}")

    def display_transaction_history(self):
        print("\n===== Transaction History =====")
        for transaction in self.transaction_history:
            print(transaction)


def main():
    user_id = input("Enter your User ID: ")
    pin = input("Enter your PIN: ")

    user_account = ATM(user_id, pin)

    if user_account.authenticate_user():
        while True:
            user_account.display_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                user_account.check_balance()
            elif choice == '2':
                amount = float(input("Enter deposit amount: $"))
                user_account.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter withdrawal amount: $"))
                user_account.withdraw(amount)
            elif choice == '4':
                amount = float(input("Enter transfer amount: $"))
                recipient_name = input("Enter recipient's name: ")
                recipient = ATM("Recipient", "1234")  # Simulated recipient with fixed User ID and PIN
                user_account.transfer(amount, recipient)
            elif choice == '5':
                user_account.display_transaction_history()
            elif choice == '6':
                print("Exiting the ATM. Thank you!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
