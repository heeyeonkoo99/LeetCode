class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[a].append(b)
        visited=[0]*numCourses

        def dfs(node):
            if visited[node]==1:
                return False
            if visited[node]==2:
                return True
            visited[node]=1
            for a in graph[node]:
                if not dfs(a):
                    return False
            visited[node]=2
            return True
        for a,b in prerequisites:
            if not dfs(a):
                return False
        return True