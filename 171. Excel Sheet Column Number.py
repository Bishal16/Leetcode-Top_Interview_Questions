class Solution:
    def titleToNumber(self, columnTitle: str) -> int:        
        charval=[chr(x) for x in range(65,91)]
        ln = len(columnTitle)
        ans=0
        
        for i in range(ln):
            ans = ans + (charval.index(columnTitle[i])+1) * (26 **(ln-i-1))
        
        return ans