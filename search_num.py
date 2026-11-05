num_list=[1,2,2,3,4,5,6,4,33,2]

num=int(input("Enter a number"))
count=0
for i in range(len(num_list)):
    if num_list[i]==num:
        count+=1
    else:
        continue

print(f"The number",num ,"appears: ",count,"times")

num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)
