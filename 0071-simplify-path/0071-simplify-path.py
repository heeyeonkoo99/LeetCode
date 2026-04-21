class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]

        
        for p in path.split("/"):
            if p=="" or p==".":
                continue
            elif p=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
            print(stack)
        return "/"+"/".join(stack)
        