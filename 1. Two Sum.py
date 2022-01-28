class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #rint('dd')
        flag = 0
        hm = {}
        for i,val in enumerate(nums):
            if target-val in hm:
                return [i,hm[target-val]]
            else:
                hm[val] = i