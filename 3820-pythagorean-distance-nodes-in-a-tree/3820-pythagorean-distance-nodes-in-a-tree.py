from collections import deque
class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        graph=[[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def bfs(start):
            dist=[-1]*n
            dist[start]=0

            q=deque([start])
            while q:
                node=q.popleft()
                for nei in graph[node]:
                    if dist[nei]==-1:
                        dist[nei]=dist[node]+1
                        q.append(nei)
            return dist
        dx=bfs(x)
        dy=bfs(y)
        dz=bfs(z)
        answer=0
        for i in range(n):
            a,b,c=sorted([dx[i],dy[i],dz[i]])
            if a*a+b*b==c*c:
                answer+=1
        return answer

        