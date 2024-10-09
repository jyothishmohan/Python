list=[1,2,3,4,5,6,7,8,9]

print("list before swap",list)
if len(list)>=2:
    first_element=list[0]
    last_element=list[-1]

    list[0]=last_element
    list[-1]=first_element
    

print("New list after swap:",list)
