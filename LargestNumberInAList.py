#1st Solution

numbers = [2, 4, 1, 5, 3, 8]
temp=0
for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

#largest Number printing
print(numbers[len(numbers)-1])
#sorted Order
for i in range(0,len(numbers)):
    print(numbers[i], end=" ")

#2nd Solution

numbers = [2, 4, 1, 5, 3, 8]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number

print(max)