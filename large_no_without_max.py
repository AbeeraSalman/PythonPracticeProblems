list_numbers=[1,2,3,4,5,55,23,41,32,8]
maximum=list_numbers[0]
for i in range(len(list_numbers)):
    if list_numbers[i] > maximum:
        maximum=list_numbers[i]


print(maximum)