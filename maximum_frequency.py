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
max_freq_val=max(counts.values())
for i in counts:
    if counts[i]==max_freq_val:
        print(i)
max_freq_key=max(counts, key=counts.get)
print("Maximum frequency is: ")
print(max_freq_key)
print(max_freq_val)


