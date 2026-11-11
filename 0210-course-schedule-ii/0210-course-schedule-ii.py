class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph=[[] for i in range(numCourses)]
        visited=[0]*(numCourses)
        res=[]
        for a,b in prerequisites:
            graph[a].append(b)
        def dfs(node):
            if visited[node]==2:
                return True
            if visited[node]==1:
                return False
            visited[node]=1
            for i in graph[node]:
                if not dfs(i):
                    return False
            visited[node]=2
            res.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
            


        return res