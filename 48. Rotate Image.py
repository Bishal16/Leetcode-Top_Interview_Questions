class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m1 = []
        for i in range(n):
            for j in range(n):
                #print("")
                m1.append(matrix[n-j-1][i])
        x = 0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = m1[x]
                x+=1
        return matrix
        