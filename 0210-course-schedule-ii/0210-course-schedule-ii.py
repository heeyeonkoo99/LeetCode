from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for dest,src in prerequisites:
            graph[src].append(dest)
        visited=[0]*numCourses
        order=[]

        def dfs(node):
            if visited[node]==1:
                return False
            if visited[node]==2:
                return True
            visited[node]=1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited[node]=2
            order.append(node)
            return True
        for i in range(numCourses):
            if visited[i]==0 and not dfs(i):
                return []
        return order[::-1]


        