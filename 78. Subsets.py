class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        ln = len(nums)
        checker = ''
        
        for i in range(ln):
            checker = checker + '0'
            
        res.append([])
        
        for i in range (2**ln-1):
            j = ln-1
            while checker[j] == '1':
                checker = checker[0:j] + '0' + checker[j+1:]
                j-=1
            
            checker = checker[0:j] + '1' + checker[j+1:]
            print(checker)
            
            j=ln-1
            s=[]
            while j>=0:               
                if checker[j] == '1':                    
                    s.append(nums[ln-j-1])
                j-=1
            #if len(s)!=0:
            res.append(s)
            
        return res