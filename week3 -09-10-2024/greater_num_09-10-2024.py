a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
c=int(input("Enter Third Number : "))

if((a>b) and (a>c)):
      print(" First is greater : ",a)
elif((b>a) and (b>c)):
    print(" Second is greater : ",b)
elif(a==b==c):
    print(" All numbers are equal")
else:
    print(" Third is greater : ",c)
    
