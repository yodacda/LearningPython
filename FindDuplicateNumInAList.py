numbers = [1, 1, 4, 5, 3, 2, 5, 8, 9,4,14, 7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)

