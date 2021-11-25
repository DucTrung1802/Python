# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method  which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details.
# Give the complete code for the  BankAccount class.

class BankAccount(object):
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = str(name)
        self.balance = balance

    def Deposit(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
            print("Deposited %d" % (amount))

        else:
            print("Balance is smaller than deposit amount!")

    def Withdrawal(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
            print("Withdrawed %d" % amount)
        else:
            print("Balance is not enough!")

    def BankFees(self, percentage):
        if (self.balance > 0):
            self.balance *= (1-percentage/100)
            print("Applied fees %.2f %%" %(percentage))
        else:
            print("Balance is not enough, the fee will be accumulated!")

    def display(self):
        print("Bank account: %d" %(self.account_number))
        print("Name: %s" %(self.name))
        print("Balance: %d" %(self.balance))


def main():
    a = BankAccount(1234, "Trung", 1000)
    a.Deposit(100)
    a.Withdrawal(100)
    a.BankFees(5)
    print()
    a.display()

if __name__ == '__main__':
    main()
