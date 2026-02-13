import textwrap
def textwrp(string , max_width):
    return textwrap.fill(string,max_width)
if __name__=="__main__":
    string=input('enter a string : ')
    max_width=int(input())
    print(textwrp(string,max_width))
    