sentence=input("Enter a sentence : ")
words=sentence.lower() .split()
b={}
for i in words:
    b[i]=b.get(i,0)+1
print(b)    
