class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            raise ValueError("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                raise ValueError("Insufficient funds.")
        else:
            raise ValueError("Invalid amount for withdrawal.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}\nBalance: ${self.balance}"


def main():
    print("Welcome to the Virtual Bank!")

    # Create bank accounts based on user input
    account_holder1 = input("Enter the account holder's name for Account 1: ")
    account_holder2 = input("Enter the account holder's name for Account 2: ")
    account1 = BankAccount(account_holder1)
    account2 = BankAccount(account_holder2)

    print("\nInitial Account Information:")
    print(account1)
    print(account2)

    try:
        # Perform transactions based on user input
        deposit_amount1 = float(input(f"Enter the deposit amount for {account1.account_holder}: $"))
        account1.deposit(deposit_amount1)

        deposit_amount2 = float(input(f"Enter the deposit amount for {account2.account_holder}: $"))
        account2.deposit(deposit_amount2)

        withdraw_amount1 = float(input(f"Enter the withdrawal amount for {account1.account_holder}: $"))
        account1.withdraw(withdraw_amount1)

        withdraw_amount2 = float(input(f"Enter the withdrawal amount for {account2.account_holder}: $"))
        account2.withdraw(withdraw_amount2)
    except ValueError as e:
        print(f"Error: {e}")
        return

    print("\nUpdated Account Information:")
    print(account1)
    print(account2)


if __name__ == "__main__":
    main()
