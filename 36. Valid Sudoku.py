class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row
        for i in range(9):
            sett = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] not in sett:
                    sett.add(board[i][j])
                    #print(sett)
                else:
                    return False
        print(1)
        #check column 
        for i in range(9):
            sett = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif board[j][i] not in sett  :
                    sett.add(board[j][i])                    
                else:
                    return False
        print(2)
        #check sub boxes
        for i in range(3):
            for j in range(3):
                sett = set()
                
                for ii in range(i*3, (i+1)*3):
                    for jj in range(j*3, (j+1)*3):
                        
                        #print(ii,jj, end ="__")
                        
                        
                        if board[ii][jj] == '.':
                            continue
                        if board[ii][jj] not in sett :
                            sett.add(board[ii][jj])
                        else:                            
                            return False
                
        return True
                
                
                
                
                
                
                
                
                
                
                
                