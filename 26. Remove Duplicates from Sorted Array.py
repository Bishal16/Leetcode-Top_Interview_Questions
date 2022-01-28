class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x,y=0,1
        
        if len(nums)==1:
            return 1
        while y < len(nums):
            if nums[x] == nums[y]:
                y+=1
            else:
                nums[x+1] = nums[y]
                x+=1
                y+=1   
        return x+1