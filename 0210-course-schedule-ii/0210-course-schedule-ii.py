class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[a].append(b)
        visited=[0]*numCourses
        res=[]

        def dfs(node):
            if visited[node]==1:
                return False
            if visited[node]==2:
                return True
            visited[node]=1
            for a in graph[node]:
                if not dfs(a):
                    return False
            res.append(node)
            visited[node]=2
            return True 
        for i in range(numCourses):
            if visited[i]==0 and not dfs(i):
                return []

            


        return res

        