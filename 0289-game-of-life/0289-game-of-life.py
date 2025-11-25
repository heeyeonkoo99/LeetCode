class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        
        # 8방향
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for dx, dy in dirs:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in [1,3]:
                        live_neighbors += 1
                
                # rule 적용
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = 3  # 1->0
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2  # 0->1
        
        # 최종 상태로 바꾸기
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
