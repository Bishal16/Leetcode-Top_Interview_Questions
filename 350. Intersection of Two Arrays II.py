class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res =  []
        hash = {}
        for i in nums1:
            if i not in hash:
                hash[i]=1
            else:
                hash[i]+=1
            
        for i in nums2:
            if i in hash:            
                res.append(i)
                hash[i]-=1
                if hash[i]==0:
                    hash.pop(i)
        return res