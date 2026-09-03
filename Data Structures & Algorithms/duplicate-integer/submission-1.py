class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)
        return False