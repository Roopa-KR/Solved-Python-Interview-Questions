class payment():
    def pay(self , amount):
        print("Processing payment of",amount)
class creditcard(payment):
    def pay(self , amount): # merthod overridong
        print("Processing payment of",amount,"using credit card")
class upi(payment):
    def pay(self , amount):# method overriding
        print("Processing payment of",amount,"using upi")
p1=creditcard()
p1.pay(1000)
p2=upi()
p2.pay(3000)