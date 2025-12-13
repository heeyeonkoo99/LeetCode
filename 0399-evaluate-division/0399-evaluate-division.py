class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(dict)
        for (A,B),val in zip(equations, values):
            graph[A][B]=val
            graph[B][A]=1/val
        def dfs(start,end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start==end:
                return 1.0
            visited.add(start)

            for neighbor, val in graph[start].items():
                if neighbor in visited:
                    continue
                temp=dfs(neighbor, end, visited)
                if temp!=-1:
                    return val*temp
            return -1.0
        results=[]
        for C,D in queries:
            results.append(dfs(C,D, set()))
        return results        