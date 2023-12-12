def max_value(word):
    vowels = 'aeiou'
    values = {'b': 1, 'c': 2, 'd': 3, 'f': 4, 'g': 5, 'h': 6, 'j': 7, 'k': 8, 'l': 9, 'm': 10, 'n': 11, 'p': 12, 'q': 13, 'r': 14, 's': 15, 't': 16, 'v': 17, 'w': 18, 'x': 19, 'y': 20, 'z': 21}

    # split word into consonant groups
    consonant_groups = [[]]
    for char in word:
        if char in vowels:
            consonant_groups.append([])
        else:
            consonant_groups[-1].append(values[char])

    # remove empty groups at start and end
    while not consonant_groups[0]:
        consonant_groups.pop(0)
    while not consonant_groups[-1]:
        consonant_groups.pop()

    # find max sum in each group and add them up
    max_sum = 0
    for group in consonant_groups:
        max_sum += sum(group)

    return max_sum

print(max_value("zodiacs")) # Output: 26
print(max_value("strength")) 
print(max_value("eight")) 
print(max_value("alpha")) 
print(max_value("charlie")) 