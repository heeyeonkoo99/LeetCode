class Solution:
    def isValid(self, s: str) -> bool:
        stack={"}":"{", "]":"[", ")":"("}
        temp=[]
        for i in s:
            if i in stack.values():
                temp.append(i)
            else:
                if not temp:
                    return False
                if temp and temp[-1] ==stack[i]: # i랑 temp[-1] 간의 관계를 잘 정립해야함! 조건을 잘게 쪼개자
                    temp.pop()
                else:
                    return False
        return len(temp)==0