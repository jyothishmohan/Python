list1=[1,2,3,4,5,6,7]
list2=[4,5,6,7,8,9,110]

if(len(list1)==len(list2)):
   print("Lists are of same length")
else:
    print("Lists are of different length")

if(sum(list1)==sum(list2)):
   print("Lists sums to same value")
else:
    print("Lists sums to different value")

common_numbers=set(list1).intersection(set(list2))

if common_numbers:
    print("Common numbers : ",common_numbers)
else:
    print("There are no elements in common")

