class creditcard:
    def pay(self , amount): 
        print("Processing payment of",amount,"using credit card")
class upi:
    def pay(self , amount):
        print("Processing payment of",amount,"using upi")
class wallet:
    def pay(self , amount):
        print("Processing payment of",amount,"using upi")
def make_payment(method , amount):
    method.pay(amount)
c=creditcard()
u=upi()
w=wallet()
make_payment(c,100)
make_payment(u,3000)
make_payment(w,8000)