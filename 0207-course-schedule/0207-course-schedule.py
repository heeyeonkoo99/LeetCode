class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph=defaultdict(list)
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
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        