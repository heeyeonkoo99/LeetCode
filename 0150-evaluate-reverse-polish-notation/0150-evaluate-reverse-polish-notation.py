class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations={"+","-","*","/"}
        for i in tokens:
            if i not in operations:
                stack.append(int(i))
            else:
                a=stack.pop()
                b=stack.pop()
                if i=="+":
                    stack.append(a+b)
                elif i=="-":
                    stack.append(a-b)
                elif i=="*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack[-1]
