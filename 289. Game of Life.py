class Solution:
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        b = []
        for i in board:
            b.append(list(i))
        c = len(board[0])
        r = len(board)
        
        def validity(x,y):
            if (x<0 or y<0 or x>=r or y>=c):
                return False
            else:
                return True        
        for i in range(r):            
            for j in range(c):
                s = 0
                #check 8 neighbour
                if validity(i+1, j):
                    if b[i+1][ j] == 1:
                        s+=1
                if validity(i+1, j+1):                    
                    if b[i+1][ j+1] == 1:
                        s+=1
                if validity(i+1, j-1):
                    if b[i+1][ j-1] == 1:
                        s+=1
                if validity(i  , j+1):
                    if b[i  ][ j+1] == 1:
                        s+=1
                if validity(i  , j-1):
                    if b[i  ][ j-1] == 1:
                        s+=1
                if validity(i-1, j-1):
                    if b[i-1][ j-1] == 1:
                        s+=1
                if validity(i-1, j):
                    if b[i-1][ j] == 1:
                        s+=1
                if validity(i-1, j+1):
                    if b[i-1][ j+1] == 1:
                        s+=1           
                #given 4 condition
                if b[i][j] == 1 and  s < 2:
                    board[i][j] = 0 
                elif b[i][j] == 1 and (s == 2 or s == 3):
                    board[i][j] = 1
                elif b[i][j] == 1 and  s > 3:
                    board[i][j] = 0
                elif b[i][j] == 0 and s == 3:
                    board[i][j] = 1  
                
                 
