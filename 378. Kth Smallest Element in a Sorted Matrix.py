class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        ls = []
        for i in range(n):
            for j in range(n):
                ls.append(matrix[i][j])
        ls.sort()        
        return(ls[k-1])