
name1 = input("Enter the first name:").lower()
name2 = input("Enter the second name:").lower()

if len(name1) != len(name2):
    print("These strings are not anagrams.")

else:
    counts = {}


    for i in name1:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1


    for i in name2:
        if i in counts:
            counts[i] -= 1
        else:
            counts[i] = -1

    # Check whether all frequencies are zero
    if all(value == 0 for value in counts.values()):
        print("These strings are anagrams.")
    else:
        print("These strings are not anagrams.")
