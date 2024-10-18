string=input("Enter the string : ")

if len(string)>=2:
    string=string[-1]+string[1:-1]+string[0]
    print("After swap :",string)
else:
    print("Swaping is not possible")
