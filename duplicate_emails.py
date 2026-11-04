users = [
    {"name": "Ali", "email": "ali@gmail.com"},
    {"name": "Sara", "email": "sara@gmail.com"},
    {"name": "Ahmed", "email": "ali@gmail.com"},
    {"name": "John", "email": "john@gmail.com"},
    {"name": "Usman", "email": "sara@gmail.com"},
    {"name": "Zara", "email": "ali@gmail.com"}
]

count=0
new_users=set()
for user in users:
    if user["email"] in new_users:
        count+=1
    else:
        new_users.add(user["email"])
print("Total number of users is: ", count ,"Unique emails are: ",new_users)


new_users_dict={}
count1=0
for user in users:
    if user["email"] in new_users_dict:
        count1+=1
        new_users_dict[user["email"]]=count1
    else:
        new_users_dict[user["email"]]=1

for key,value in new_users_dict.items():
    print(key,":",value)



for k,v in new_users_dict.items():
    print("Duplicate Emails: ")
    if v>1:
        print(k,":",v)


