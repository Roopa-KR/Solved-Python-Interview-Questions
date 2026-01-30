# Split the string and join using '-'
def split_join(line):
    splitted=line.split()
    joined="-".join(splitted)
    return joined
if __name__=="__main__":
    line=input("enter the characters")
    result=split_join(line)
    print(result)