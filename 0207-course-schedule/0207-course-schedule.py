class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for  _ in range(numCourses)]
        for a,b in prerequisites:
            graph[a].append(b)


        visited=[0] *numCourses
        def dfs(i):
            if visited[i]==1:
                return False
            if visited[i]==2:
                return True
            visited[i]=1
            for c in graph[i]:
                if not dfs(c):
                    return False
            visited[i]=2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        