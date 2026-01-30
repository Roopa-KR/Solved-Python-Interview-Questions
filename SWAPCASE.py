# Changing the case of each character in a string

def swap_case(data):
        swapped=""
        for char in data:
            if char.isupper():
                swapped+=char.lower()
            elif char.islower():
                swapped+=char.upper()
            else:
                swapped+=char
        return swapped
if __name__=="__main__":
    data=input("enter the characters")
    result=swap_case(data)
    print(result)