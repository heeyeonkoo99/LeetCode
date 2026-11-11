class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph=defaultdict(list)
        visited=[0]*numCourses
        for a,b in prerequisites:
            graph[a].append(b)

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
            res.append(node)
            return True
        
        res=[]
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        