class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftover = []
        leftover.append(nums[0])
        rightover = []
        rightover.append(nums[-1])
        
        ln = len(nums)
        
        for i in range(1,ln):
            leftover.append(leftover[-1]*nums[i])
        
        for i in range(ln-2, -1, -1):            
            rightover.insert(0, rightover[0]*nums[i])
            
        res= []
        res.append(rightover[1]) #first element
        for i in range(1, ln-1):
            res.append(leftover[i-1] * rightover[i+1])
        res.append(leftover[ln-2])
        return res
        