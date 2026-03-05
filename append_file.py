with open("demo/pfile.py" ,"a") as f:
    f.write("\nWelcome to Python programming!")
with open("demo/pfile.py" ,"r") as f:
    data=f.read()
    print(data)
    f.close()