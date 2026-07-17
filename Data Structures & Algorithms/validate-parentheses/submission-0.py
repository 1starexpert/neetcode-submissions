class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for symbol in s:
            stack.append(symbol)
            second_last = stack[len(stack) - 2]
            if second_last == "{" and symbol == "}":
                stack.pop()
                stack.pop()
            if second_last == "(" and symbol == ")":
                stack.pop()
                stack.pop()
            if second_last == "[" and symbol == "]":
                stack.pop()
                stack.pop()
        if len(stack) == 0:
            return True
        return False

        