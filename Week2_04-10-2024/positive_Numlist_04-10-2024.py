list1=[]
list2=[]
size=int(input("Enter size of the list : "))
for i in range(size):
    elements=int(input(f"Enter element {i+1} : "))
    list1.append(elements)
for i in list1:
    if(i>0):
        list2.append(i)
print("New list of positive numbers = ",list2)
        
