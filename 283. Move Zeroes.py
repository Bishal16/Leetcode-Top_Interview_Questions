class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        ln = len(nums)
        while i < ln:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                i-=1
                ln-=1
            
            i+=1
        return nums