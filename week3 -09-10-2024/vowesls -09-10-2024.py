string=input("Enter string : ")
vowels=["a","A","e","E","i","I","o","O","u","U"]
found=[]
for i in string:
    if( i in vowels):
        found.append(i)
if found:
    print("Vowels are : ",found)
else:
    print("No vowels are present")
        

