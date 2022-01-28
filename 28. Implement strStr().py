class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ln=len(needle)
        if needle=='' or haystack==needle :
            return 0

        else:
            for i in range(len(haystack)-ln+1):
                c=0
                for j in range(ln): 
                    if haystack[i]!=needle[j]:
                        break
                    else:
                        c+=1
                        i+=1
                        
                        if c==ln:
                            return i-ln
            
            return -1
                    