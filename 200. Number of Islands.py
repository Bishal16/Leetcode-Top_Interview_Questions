class Solution:
         
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        r = len(grid)
        c = len(grid[0])
        visited = []
        for i in range(r):  # creating a matrix filled with 0 ( represents unvisited node)
            t=[]
            for j in range(c):
                t.append(0)
            visited.append(t)
            
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and visited[i][j] == 0 : # if it is a island(1) and not visited yet then make it visited and continue for adjacen island
                    visited[i][j] = 1
                    island+=1
                    def check(i,j):
                        #right node
                        if j < c-1:
                            if grid[i][j+1] == "1" and visited[i][j+1] == 0:
                                visited[i][j+1] = 1
                                check(i, j+1)
                        #bottom node
                        if i < r-1:                            
                            if grid[i+1][j] == "1" and visited[i+1][j] == 0:
                                visited[i+1][j] = 1
                                check(i+1, j)
                        #left node
                        if j > 0:
                            if grid[i][j-1] == "1" and visited[i][j-1] == 0:
                                visited[i][j-1] = 1
                                check(i, j-1)
                        #top node
                        if i > 0:
                            if grid[i-1][j] == "1" and visited[i-1][j] == 0:
                                visited[i-1][j] = 1
                                check(i-1, j)
                    
                    check(i,j)
        return island
    