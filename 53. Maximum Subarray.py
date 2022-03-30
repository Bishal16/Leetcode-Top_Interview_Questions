class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -10**10
        curSum = 0
        
        maxx = maxSum
        for i in range(len(nums)):
            curSum = curSum + nums[i]
            
            if curSum < 0:
                curSum = 0
            if curSum > maxSum:
                maxSum = curSum
                
            if nums[i] > maxx:
                maxx = nums[i]
        if maxSum == 0:
            maxSum = maxx#(nums)
        return maxSum