# in : [1, 2, 3, 4] -> [24, 12, 8, 6] : out
# Time complexity O(n), but division by zero error

class Giveme:
    def getArray(self, array:list[int]) -> list[int]:
        product = 1 
        for i in array:
            product *= i
        newList = []
        for element in array:
            newList.append(int(product/element))
        return newList
    
result = Giveme()
print(result.getArray([1, 2, 3, 4]))

#===============================================================================#
# Time complexity :O(n),space complexity :O(n), no case error
# in : [1, 2, 3, 4] -> [24, 12, 8, 6] : out
# leftArray  : start-> [1, 1, 1, 1] : end ->   [1, 1, 2, 6]
# rightArray : start-> [1, 1, 1, 1] : end ->   [1, 4, 12, 24]
#             index -> [0  1  2  3]   index -> [0  1   2  3]    
       
class Google:
    def getArray(self, array : list[int])->list[int]:
        n = len(array)
        leftArray, rightArray = [1]*n, [1]*n
        result = []
        for i in range(1, n):
            leftArray[i] = leftArray[i-1] * array[i-1]
            rightArray[i] = rightArray[i-1]* array[::-1][i-1]
        for i in range(n):
            result.append(leftArray[i]*rightArray[::-1][i])
        print("\n")
        print(f"The left array is : {leftArray}", end=" ")
        print(f"The right array is : {rightArray}", end=" ")
        print(f"The resultant array is : {result}", end=" ")
        print("\n")
        return result
    
g1= Google()
print(g1.getArray([1, 2, 3, 4]))

# Time complexity :O(n),space complexity :O(1), no case error
class Googleg:
    def getArrayg(self, array : list[int])->list[int]:
        n = len(array)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= array[i]
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= array[i]
        return res
g2 = Googleg()
print(g2.getArrayg([1, 2, 3, 4]))

            
