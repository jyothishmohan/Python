list1=[]
dict1={}
size=int(input("Enter number of firstnames to be added : "))

for i in range(size):
         fnames=input(f"Enter first name {i+1} : ")
         list1.append(fnames)
for i in list1:
         count=i.lower().count("a")
         dict1[i]=count

print("first names : ",list1)
print('Number of occurances of "a" : ',dict1)
print("Total occurance of 'a' : ",sum(dict1.values()))
         
