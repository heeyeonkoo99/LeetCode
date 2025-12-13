class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        def get_value(s):
            quot,rem=divmod(s-1,n)
            row=n-1-quot
            col=rem if (n-1-row)%2==0 else n-1-rem
            return board[row][col]
        visited=set()
        queue=deque([(1,0)])
        visited.add(1)

        while queue:
            pos,moves=queue.popleft()
            if pos==n*n:
                return moves
            for i in range(1,7):
                next_pos=pos+i
                if next_pos>n*n:
                    continue
                val=get_value(next_pos)
                if val!=-1:
                    next_pos=val
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos,moves+1))
        return -1
        