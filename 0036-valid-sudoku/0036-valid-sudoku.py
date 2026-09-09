class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        col=defaultdict(set)
        box=defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                else:
                    if board[i][j] in row[i//3] or board[i][j] in col[j//3] or board[i][j] in box[(i//3, j//3)]:
                        return False
                    row[i//3].add(board[i][j])
                    col[j//3].add(board[i][j])
                    box[(i//3, j//3)].add(board[i][j])
                
        return True
                
        