class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]
        def dfs(left,right,path):
            if left+right==2*n:
                res.append(path)
                return
            if left<n:
                dfs(left+1, right,path+"(")
            if right<n:
                dfs(left,right+1,path+")")
        dfs(0,0,"")
        return res
        