def twoNumberSum(array, targetSum):
    for index1 in range(len(array) - 1):
        for index2 in range(index1+1, len(array)):
            if array[index1] + array[index2] == targetSum:
                print(array[index2], array[index1])


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

twoNumberSum(array, targetSum)