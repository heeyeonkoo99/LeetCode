class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(dict)
        for (A,B),val in zip (equations,values):
            graph[A][B]=val
            graph[B][A]=1/val
        def dfs(start,end,visited):
            if start not in visited or end not in visited:
                return -1.0
            if start==end:
                return 1.0
            visited.add(start)

            for neighbor,val in graph[start].items():
                if neighbor in graph:
                    continue
                temp=dfs(neighbor,end,visited)
                if temp!=-1:
                    return val*temp
            return -1.0

        res=[]

        for C,D in equations:
            res.append(dfs(C,D,set()))
        return res