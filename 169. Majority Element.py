class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        keys = list(hash.keys())
        vals = list(hash.values())
        max_key = max(hash, key=hash.get)
        return(keys[vals.index(max(vals))])        