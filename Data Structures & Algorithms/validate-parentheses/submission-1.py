class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if stack:
                if item == ")" and stack[-1] == "(":
                    stack.pop()
                elif item == "]" and stack[-1] == "[":
                    stack.pop()
                elif item == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(item)
            else:
                stack.append(item)
        if len(stack) == 0:
            return True
        return False