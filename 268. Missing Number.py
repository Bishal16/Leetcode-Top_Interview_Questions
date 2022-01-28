class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash = {}
        for i in nums:
            hash[i] = i
        for i in range(len(nums)+1):
            if i not in hash:
                return i
                
            