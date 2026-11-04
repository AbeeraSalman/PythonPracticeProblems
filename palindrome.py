name=input("Enter the string to check either its palindrome or not: ").lower()

reverse=name[::-1]
if name==reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

