class Solution:
    def isValid(self, s: str) -> bool:
        stack={"}":"{", "]":"[", ")":"("}
        temp=[]
        for i in s:
            if i in stack.values():
                temp.append(i)
            else:
                if temp and stack[i]==temp[-1]:
                    temp.pop()
                else:
                    return False
        if len(temp)==0:
            return True
        return False

