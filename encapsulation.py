#encapsulation
class bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
acc=bankaccount(0)
acc.deposit(6000)
print(acc.get_balance())