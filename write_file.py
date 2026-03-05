with open("demo/pfile.py" ,"w") as f:
    f.write("Hello, World!")
with open("demo/pfile.py" ,"r") as f:
    data=f.read()
    print(data)
    f.close()