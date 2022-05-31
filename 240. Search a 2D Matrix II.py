class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix)
        for i in range(r):
            if target in matrix[i]:
                return True                
        return False