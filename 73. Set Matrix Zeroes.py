class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        zeros_r = set()
        zeros_c = set()
        #finding the row and column to make zero
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    zeros_r.add(i)
                    zeros_c.add(j)
        # make selected rows zero
        for i in zeros_r:
            for j in range(c):
                matrix[i][j] = 0
        # make selected columns zero
        for i in zeros_c:
            for j in range(r):
                matrix[j][i] = 0