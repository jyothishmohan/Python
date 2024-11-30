dict1={}
dict1['Name']=input("Enter the name:")
dict1['Roll number']=input("Enter the roll number:")
dict1['registration number']=input("Enter the registration number:")
dict1['Department']=input("Enter the Department:")
dict1['Semester']=input("Enter the semester:")
print("Dictionary : ",dict1)
print()
print()

totalmark=int(input("Enter the total mark out of 100:"))
print("Total mark= ",totalmark)
print()
print()
dict1['total mark']=totalmark
print()
print("Dictionary after adding total mark:",dict1)
print()

if dict1['total mark']>=90:
    dict1['grade']='A'
    
elif dict1['total mark']>=82:
    dict1['grade']='B'
    
elif dict1['total mark']>=75:
    dict1['grade']='C'
    
elif dict1['total mark']>=60:
    dict1['grade']='D'
    
elif dict1['total mark']>=50:
    dict1['grade']='P'
else:
    dict1['grade']='FAILED'
print("Dictionary after adding grade:",dict1)
print()

dict1.pop('Roll number')
print("Dictionary after deleting roll number:",dict1)
