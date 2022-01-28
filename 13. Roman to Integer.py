class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        grp = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900 }
        
        i=0
        ans = 0
        while(i<len(s)):
            t = s[i:i+2]
            if t in grp:
                ans = ans + grp[t]
                i = i + 2
            else:
                ans = ans + val[t[0]]
                i = i + 1
        return ans
                
            
        