class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash = {}
        for i in nums1:
            for j in nums2:
                if 0-(i+j) not in hash:
                    hash[0-(i+j)] = 1
                else:
                    hash[0-(i+j)] += 1        
        c=0
        for i in nums3:
            for j in nums4:
                if (i+j) in hash:
                    c+=hash[i+j]                            
        return c
