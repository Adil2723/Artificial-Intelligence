class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print("Amount deposited", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("Amount withdrawn", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        print("Current balance", self.__balance)


account1 = BankAccount("Alice", "ACC101", 7000)
account2 = BankAccount("Bob", "ACC102", 2000)

account1.deposit(9000)
account1.withdraw(5000)
account1.get_balance()

account2.deposit(500)
account2.withdraw(3000)
account2.get_balance()
