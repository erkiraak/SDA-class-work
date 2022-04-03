from dataclasses import dataclass
import pickle
import atexit


class CustomerDatabase:
    def __init__(self):
        self.database_filename = "decorator_transfer_customer_data.pickle"
        self.customers = []
        self.load_customer_data()

    def add_customer(self, customer):
        if self.customers:
            for existing_customer in self.customers:
                if existing_customer == customer:
                    print("Customer already exists")
                    return
        self.customers.append(customer)
        self.save_customer_data()

    def save_customer_data(self):
        with open(self.database_filename, 'wb') as f:
            pickle.dump(self.customers, f)

    def load_customer_data(self):
        try:
            with open(self.database_filename, 'rb') as f:
                self.customers = pickle.load(f)
        except FileNotFoundError:
            pass


@dataclass
class Customer:
    name: str
    balance = 0
    loan_remainder = 0
    loan_remainder_months = 0
    monthly_payment = 0

    def give_loan(self, amount, months):
        self.balance += amount
        self.loan_remainder = amount
        self.loan_remainder_months = months
        self.calculate_monthly_payment()

    def repay_loan_monthly(self):
        self.loan_remainder -= self.monthly_payment
        self.loan_remainder_months -= 1

    def add_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        self.balance -= amount

    def calculate_monthly_payment(self):
        self.monthly_payment = self.loan_remainder / self.loan_remainder_months

    def __repr__(self):
        return f"name: {self.name}\n" \
               f"balance = {self.balance}\n" \
               f"loan_remainder = {self.loan_remainder}\n" \
               f"loan_remainder_months = {self.loan_remainder_months}\n" \
               f"monthly_payment = {self.monthly_payment}\n"


@atexit.register
def save_customer_data():
    customer_database.save_customer_data()


def find_customer(name):
    if name is None:
        return None
    for customer in customer_database.customers:
        if name.title() == customer.name:
            return customer
    print("Customer not found")
    return None


def check_amount(amount):
    try:
        amount = float(amount)
        if amount < 3000:
            raise ZeroDivisionError
    except ValueError:
        print("Invalid amount")
        return None
    except ZeroDivisionError:
        print("Amount has to at least than 3000")
        return None
    except TypeError:
        return None
    else:
        return amount


def check_time(months):
    try:
        months = int(months)
        if months < 3:
            raise ZeroDivisionError
    except ZeroDivisionError:
        print("Loan duration has to be at least 3 months")
        return None
    except ValueError:
        print("Invalid number of months")
        return None
    except TypeError:
        return None
    else:
        return months


def check_transfer(func):
    def wrapper(*args, **kwargs):
        amount = args[0]
        balance = args[1].balance

        if balance >= amount:
            func(*args, **kwargs)
        else:
            print("Insufficient funds to complete transaction")

    return wrapper


@check_transfer
def transfer(amount, transfer_from, transfer_to):
    transfer_from.withdraw_money(amount)
    transfer_to.add_money(amount)
    print(f"Transfer validated, ${amount} has been transferred from {transfer_from.name} to {transfer_to.name}")
    print(f"{transfer_from.name} has a remaining account balance of {transfer_from.balance}")
    print(f"{transfer_to.name} has a new account balance of {transfer_to.balance}")
    print("Thank you for banking with us")


def check_loan_eligibility(func):
    def wrapper(*args, **kwargs):
        loan_amount = args[0]
        loan_duration = args[1]
        customer = args[2]
        balance = args[2].balance
        if customer.loan_remainder:
            print("Loan denied, customer needs to pay back previous loan before applying for another")
        elif (balance / 12 >= loan_amount / loan_duration):
            func(*args, **kwargs)
        else:
            print("Account balance insufficient for loan")

    return wrapper


@check_loan_eligibility
def give_loan(amount, loan_duration, customer):
    customer.give_loan(amount, loan_duration)
    print(f"Loan approved, ${amount} has been transferred {customer.name}'s account.")
    print(f"The monthly payment will be {customer.monthly_payment} for {customer.loan_remainder_months} months")


def make_payment(transfer_from=None, transfer_to=None, amount=None):
    transfer_from = find_customer(transfer_from)
    transfer_to = find_customer(transfer_to)
    amount = check_amount(amount)

    while not transfer_from:
        transfer_from = find_customer(input("Please insert name of person doing the transfer: "))
    while not transfer_to:
        transfer_to = find_customer(input("Please insert name of person money is being transferred to: "))
        if transfer_from == transfer_to:
            print("From and to accounts are the same, please try again")
            transfer_to = None
    while not amount:
        amount = check_amount(input("Please insert amount to transfer: "))

    transfer(amount, transfer_from, transfer_to)


def apply_for_loan(customer=None, amount=None, loan_duration=None):
    customer = find_customer(customer)
    amount = check_amount(amount)
    loan_duration = check_time(loan_duration)

    while not customer:
        customer = find_customer(input("Please insert name of person applying for loan: "))
    while not amount:
        amount = check_amount(input("Please insert loan amount: "))
    while not loan_duration:
        loan_duration = check_time(input("Please loan duration: "))

    give_loan(amount, loan_duration, customer)


customer_database = CustomerDatabase()

# customer_database.add_customer(Customer("Erki"))
# find_customer("john").add_money(100000)
# find_customer("iris").withdraw_money(1000)
# make_payment("erki", "iris", 10000)
# apply_for_loan(customer="john", amount=100000, loan_duration=360)

for cust in customer_database.customers:
    print(cust)
