sub1=int(input("Enter Mark of subject 1 : "))
sub2=int(input("Enter Mark of subject 2 : "))
sub3=int(input("Enter Mark of subject 3 : "))
sub4=int(input("Enter Mark of subject 4 : "))
sub5=int(input("Enter Mark of subject 5 : "))

max_mark=500
total_mark=(sub1+sub2+sub3+sub4+sub5)
percentage=(total_mark/max_mark)*100

print("Total Mark : ",total_mark)
print("Percentage : ",percentage)
