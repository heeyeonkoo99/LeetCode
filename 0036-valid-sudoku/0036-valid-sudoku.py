from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row=defaultdict(set)
        col=defaultdict(set)
        mat=defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j]in mat[i//3,j//3]:
                    return False
                row[i].append(board[i][j])
                col[j].append(board[i][j])
                mat[i//3,j//3].append(board[i][j])
        return True
        