class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i, num in enumerate(nums):
            x = target - num
        
            if x in dictionary:
                return [dictionary[x], i]
            else: 
                dictionary[num] = i