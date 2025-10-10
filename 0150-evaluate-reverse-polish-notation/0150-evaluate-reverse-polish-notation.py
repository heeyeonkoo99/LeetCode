from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {"+", "-", "*", "/"}
        stack = []
        
        for token in tokens:
            if token not in operations:
                stack.append(int(token))  # 숫자를 바로 int로 저장
            else:
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # "/"
                    stack.append(int(a / b))  # trunc towards zero
        
        return stack[-1]
