class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ln = len(digits)
        if digits[ln-1] != 9:
            digits[ln-1] = digits[ln-1] + 1
            return digits
        else:
            i=-1
            c=0
            while i >= -len(digits):
                if digits[i]==9:
                    c+=1
                else:
                    break
                i-=1
            arr=[]
            if c==ln:
                arr = [0]*c
                arr.insert(0,1)
                return arr
            else:
                digits[ln-c-1] += 1
                digits = digits[0:ln-c] 
                digits = digits + [0]*c
                return digits
            
            