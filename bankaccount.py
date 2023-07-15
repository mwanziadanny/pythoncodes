class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("You have withdrawn", amount)
            print("Your current balance is", self.balance)

    def check_balance(self):
        return "The current balance is", self.balance

    def customer_details(self):
        print("Account number:", self.account_number)
        print("Name:", self.customer_name)
        print("Balance:", self.balance)
        print("Date of opening:", self.date_of_opening)


customer = BankAccount(5440, 6000, '5/02/2023', "Maxwell")
customer.customer_details()
customer.deposit(1000)
customer.check_balance()
customer.withdraw(500)
customer.check_balance()
