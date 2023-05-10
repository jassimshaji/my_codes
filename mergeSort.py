import math


def Sorted(arr):
    if len(arr) < 2:
        return arr
    middleIndex = math.floor(len(arr)/2)
    leftArr = list(arr[:middleIndex])
    rightArr = list(arr[middleIndex:])
    return sort(Sorted(leftArr), Sorted(rightArr))


def sort(leftArr, rightArr):
    resultArr = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] > rightArr[rightIndex]:
            resultArr.append(rightArr[rightIndex])
            rightIndex += 1
        else:
            resultArr.append(leftArr[leftIndex])
            leftIndex += 1
    return resultArr + list(leftArr[leftIndex:]) + list(rightArr[rightIndex:])


arr = [2, 6, 9, 1, 8, 20, 45, 42, 700, 90]
result = Sorted(arr)
print(result)
