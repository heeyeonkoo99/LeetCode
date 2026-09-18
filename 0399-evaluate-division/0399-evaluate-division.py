class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],     queries: List[List[str]]) -> List[float]:
        graph=defaultdict()
        for (a,b),v in zip(equations,values):
            graph[a][b]=v
            graph[b][a]=1/v

        def dfs(start,end,visited):
            if start not in graph and end not in graph:
                return -1.0
            if start==end:
                return 1.0
            visited.add(start)
            for neighbor,value in graph[start].items():
                if neighbor in visited:
                    continue
                temp=dfs(neighbor,end,visited)
                if temp!=-1.0:
                    return value*temp
            return -1.0




        res=[]
        for s,e in queries:
            
            res.append(dsf(s,e,set()))
        return res