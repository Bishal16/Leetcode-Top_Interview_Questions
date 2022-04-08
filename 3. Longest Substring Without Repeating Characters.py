class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        ln = len(s)
        max = 0
        for i in range(ln):
            hash = {}
            tmp = 0
            for j in range(i,ln):
                if s[j] not in hash:
                    hash[s[j]] = s[j]
                    tmp+=1
                else:                    
                    break   
            if tmp > max:
                max = tmp
            hash.clear()
        return max