class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        combined_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in combined_dict:
                return [combined_dict[complement], i]
            combined_dict[num] = i
        return []
list_of_nums = Solution()
result = list_of_nums.twoSum([-3, 4, 3, 9], 12)
print(result)

               

