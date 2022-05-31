class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {'2':'abc' , '3':'def' , '4':'ghi' , '5':'jkl' , '6':'mno' , '7':'pqrs' , '8':'tuv' , '9':'wxyz' }
        ln = len(digits)
        ans = []
        if ln == 1:
            ans = list(map[digits[0]])
        elif ln == 2:
            for i in map[digits[0]]:
                for j in map[digits[1]]:
                    ans.append(i+j)
        elif ln == 3:
            for i in map[digits[0]]:
                for j in map[digits[1]]:
                    for k in map[digits[2]]:
                        ans.append(i+j+k)
        elif ln == 4: 
            for i in map[digits[0]]:
                for j in map[digits[1]]:
                    for k in map[digits[2]]:
                        for l in map[digits[3]]:
                            ans.append(i+j+k+l)    
        return ans