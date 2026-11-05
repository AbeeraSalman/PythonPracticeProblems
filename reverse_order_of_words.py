user_inp=input("Enter a sentence:")

user_inp=user_inp.split()
for word in range(len(user_inp)-1,-1,-1):
    print(user_inp[word])
