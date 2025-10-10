class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for c in tokens:
            # if c.isnumeric():
            if c not in operations:
                stack.append(int(c))

            else:
                b = stack.pop()
                a = stack.pop()

                if c == "+":
                    stack.append(a + b)
                elif c == "-":
                    stack.append(a - b)
                elif c == "*":
                    stack.append(a * b)
                elif c == "/":
                    stack.append(math.trunc(a/b))
        return stack[-1]