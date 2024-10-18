list1=[]
size=int(input("Enter the number of integers to be added : "))

for i in range(size):
    integers=int(input(f"Enter integer {i+1}: "))
    list1.append(integers)
for i in range(len(list1)):
                 if list1[i]>100:
                      list1[i]='over'
print("List = ",list1)                 
