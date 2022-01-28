class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==1:
            return ["()"]
        res = []
        
        s = '('
        for i in range(2*n-1):
            s=s+')'
        for i in range(int((2**(2*n))/2)-1):
            flag = True
            count = 0
            
            # generate all combination
            j = 2*n-1
            while s[j] == '(':               
                s = s[0:j] + ')' + s[j+1:]
                j-=1
            s = s[0:j] + '(' + s[j+1:]
            
            
            
            #''' check validity
            stk = [] 
            for j in range(2*n):     
                if s[j] == '(':
                    stk.append('(')
                else:
                    if len(stk) == 0 :
                        stk.append(')')
                        break
                    else:
                        stk.pop()
            if len(stk) == 0 :
                res.append(s)
        return res
            #'''