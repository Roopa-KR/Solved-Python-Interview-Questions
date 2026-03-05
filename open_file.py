# create a folder named demo and create a file named pfile.py in it 
with open("demo/pfile.py" ,"r") as f:
    data=f.read()
    print(data)
# you can see blank file because we have not written anything in it yet. Now we will write some data in it and then read it again.