name= input("Enter your name: ")
name=name.lower()
counts={}
for i in name:
   if i in counts:
       counts[i]+=1
   else:
       counts[i]=1
print("Frequency for each character.")
print(counts)
