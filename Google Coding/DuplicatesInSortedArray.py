class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        k = 0
        expectedNum = [0]*n
        for i in range(n - 1):
            if nums[i] != nums[i+1]:
                expectedNum[k] = nums[i]
                k += 1
        expectedNum[k] = nums[n-1]
        k += 1
        for i in range(k):
            nums[i] = expectedNum[i]
        print(f"The list of modified nums[] is {nums[:k]}")   
        return k
duplicateList = Solution()
k = duplicateList.removeDuplicates([1, 1, 2, 3, 3, 4, 4,5 ,5 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,6 ,8 ,8 ,8 ,8])
print(f"The number of unique_elements is {k}")



