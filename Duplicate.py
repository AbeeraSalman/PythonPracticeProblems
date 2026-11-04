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


print("Duplicate characters")
for i in counts:
    if counts[i]>1:
        print(i)


#how to remove duplicates
print("Unique elements")
for i in counts:
    print(i)




