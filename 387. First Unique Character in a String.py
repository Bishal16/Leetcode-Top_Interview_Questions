class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i]+=1
        for i in range(len(s)):
            if hash[s[i]] == 1:
                return i
        return -1