class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ln = len(s) 
        
        for i in range(int(ln/2)):
            tmp = s[i]
            s[i] = s[ln-i-1]
            s[ln-i-1] = tmp
            
        