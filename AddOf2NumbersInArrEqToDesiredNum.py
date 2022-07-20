
desiredNum = 6
numArr = [3,2,3]
for i in range(0, len(numArr)):
    for j in range(i+1, len(numArr)):
        if numArr[i] + numArr[j] == desiredNum:
            print(i, j)