class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[a].append(b)
        visited=[0]*numCourses
        order=[]
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
            order.append(i)
            return True
        
        for i in range(numCourses):
            if visited[i]==0 and not dfs(i):
                return[]
        return order


        