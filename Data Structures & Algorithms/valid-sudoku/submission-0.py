class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        square = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue 
                square_idx = (r//3)*3+(c//3)
                if val in row[r] or val in column[c] or val in square[square_idx]:
                    return False 
                row[r].add(val)
                column[c].add(val)
                square[square_idx].add(val)
        return True
                    

                    
                    
                     

                
                 



        