class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as f:
            self.balance = float(f.readlines()[-1])

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance = self.balance - amount
            self.balance = round(self.balance, 2)
            self.commit("Balance after Withdrawal: ")
        else:
            print("Sorry you do not have that much money in your account ")

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.balance = round(self.balance, 2)
        self.commit("Balance after Deposit: ")

    def commit(self, message):
        with open(self.filepath, 'a') as file:
            file.write(message +'\n'+ str(self.balance)+'\n')
            file.close()

class Checking(Account):
    obj_var="checking"
# This is it's own class, but importing this class will allow you to manipulate the instance of previous object
    def __init__(self, filepath):
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance=self.balance - amount
        self.balance = round(self.balance, 2)
        self.commit("Balance after Transfer: ")

my_check = Checking("balance.txt")
my_check.transfer(99)
print(my_check.balance)
print(my_check.obj_var)


# acc = Account("balance.txt")
# print(acc.balance)
# acc.withdraw(1098.19)
# print(acc.balance)
# acc.withdraw(1000998.19)
# print(acc.balance)
# acc.deposit(109.59)
# print(acc.balance)
