class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split("/")
        res=[]
        for i in path:
            if i=="." or i=="":
                continue
            elif i=="..":
                if res:

                    res.pop()
            else:
                res.append(i)

        return "/"+"/".join(res)