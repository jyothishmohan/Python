dict1={'Name':'Jyothish','Roll Number':25, 'Registration Number':'TMATSMT032', 'Department':'MCA', 'Semester':1}
print("Dictionary : ",dict1)
print()

dict1['Total Mark']=int(input("Enter mark out of 100 : "))
print("Dictionary after adding total mark : ",dict1)
print()

if dict1['Total Mark']>=90:
    dict1['Grade']='A'

elif dict1['Total Mark']>=82:
    dict1['Grade']='B'

elif dict1['Total Mark']>=60:
    dict1['Grade']='C'

elif dict1['Total Mark']>=50:
    dict1['Grade']='P'

else:
    dict1['Grade']='F'

print("Dictionary after adding grade : ",dict1)
print()

dict1.pop('Roll Number')
print("Dictionary after deleting roll number : ",dict1)
