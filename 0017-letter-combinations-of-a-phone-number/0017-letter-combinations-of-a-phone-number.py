class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res=[]
        def dfs(i,path):
            if i==len(digits):
                res.append(path)
                return
            for d in map[int(digits[i])]:
                dfs(i+1,path+d)
        dfs(0,"")
        return res

        
        