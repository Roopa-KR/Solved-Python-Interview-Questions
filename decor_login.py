import datetime
x=datetime.datetime.now()
print(x)
def add_timings(func):
    def cover(Id,Name):
        print(f"your login timings: {x}")
        if Id==101 and Name=="abc":
            func()
        print("successfully logged in!")
    return cover
@add_timings
def login():
    print(f"{Id} : {Name}")
Id=int(input("enter your id: "))
Name=input("Enter name: ")
login(Id,Name)