user_input = input("Enter a string:")

str_list = []
longest = 0
longest_str = ""

for char in user_input:

    if char in str_list:
        index = str_list.index(char)
        str_list = str_list[index + 1:]

    str_list.append(char)

    if len(str_list) > longest:
        longest = len(str_list)
        longest_str = "".join(str_list)

print("Longest substring length:", longest)
print("Longest substring:", longest_str)