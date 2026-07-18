class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        [1, 2, +, 3, 4, *, +]
        """
        stack = []
        if len(tokens) == 0:
            return null
        if len(tokens) == 1:
            return int(tokens[0])
        for t in tokens:
            if t.lstrip("+-").isdigit():
                stack.append(t)
            else: 
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if t == "*":
                    result = num1 * num2
                if t == "+":
                    result = num1 + num2
                if t == "-":
                    result = num1 - num2
                if t == "/":
                    result = num1 / num2
                stack.append(int(result))
                print(stack)
        return stack.pop()
            
        