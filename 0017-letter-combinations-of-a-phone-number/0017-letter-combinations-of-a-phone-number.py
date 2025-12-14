class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        map={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs", 8:"tuv",9:"wxyz"}
        def dfs(i,curr):
            if len(curr)==len(digits):
                res.append(curr)
                return
            for alpha in map[int(digits[i])]:
                dfs(i+1, curr+alpha)
        if digits:
            dfs(0,"")
        return res


        