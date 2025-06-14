from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = 0  # Protected variable (Encapsulation)

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def display_info(self):
        print(f"Account: {self.account_number}, Holder: {self.account_holder}, Balance: ₹{self._balance}")


class SavingsAccount(Account):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited into Savings Account.")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"₹{amount} withdrawn from Savings Account.")
        else:
            print("Insufficient balance or invalid amount.")

# Child class - CurrentAccount (Inheritance + Polymorphism)
class CurrentAccount(Account):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)
        self.overdraft_limit = 1000  
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited into Current Account.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            print(f"₹{amount} withdrawn from Current Account.")
        else:
            print("Overdraft limit exceeded or invalid amount.")


def main():
    print("=== Banking System Demo ===")
    
    savings = SavingsAccount("S101", "Prem")
    current = CurrentAccount("C202", "Chand")


    for account in (savings, current):
        account.display_info()
        account.deposit(1000)
        account.withdraw(300)
        account.display_info()
        print()

if __name__ == "__main__":
    main()