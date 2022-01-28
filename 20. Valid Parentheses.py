class Solution:
    def isValid(self, s: str) -> bool:
        br=[]
        
        
        for i in s:
            if i == '(' or i == '{' or i == '[':
                br.append(i)
            elif i == ')' :
                if len(br)==0 or  br[-1] != '(':
                    return False
                    break
                else:
                    br.pop()
            elif i == '}' :
                if  len(br)==0 or br[-1] != '{':
                    return False
                    break
                else:
                    br.pop()
            elif i == ']' :
                if len(br)==0 or br[-1] != '[':
                    return False
                    break
                else:
                    br.pop()
                
        if len(br)== 0 :
            return True