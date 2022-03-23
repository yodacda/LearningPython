
desiredNum = 4
numArr = [2, 3, 1, 7, 4, 9, 2, 10]
for i in range(0, len(numArr)):
    for j in range(i+1, len(numArr)):
        if numArr[i] + numArr[j] == desiredNum:
            print(numArr[i], numArr[j])