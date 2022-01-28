class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
                
        res = [[1],[1,1]]
        i = 3
        while i <= numRows:
            lastRow = res[-1][:]
            lr = lastRow[:]            
            for j in range(len(lastRow)-1):
                lastRow[j+1] = lr[j] + lr[j+1]
            lastRow.append(1)
            res.append(lastRow)
            i+=1            
        return res
