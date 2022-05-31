class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x,y=0,0
        for i in range(len(nums)):
            if nums[i]==0:
                x+=1
            elif nums[i]==1:
                y+=1
        for i in range (len(nums)):
            if x>0:
                nums[i]=0
                x-=1
            elif y>0:
                nums[i]=1
                y-=1
            else:
                nums[i]=2
            