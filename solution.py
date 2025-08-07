#  ()[]{}
class Solution:
    def isValid(self, s: str) -> bool:
        # stack для хранения скобок
        stack = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)

            elif char == ")":
                try:
                    bracket = stack.pop()
                    if bracket != "(":
                        return False
                except:
                    return False

            elif char == "]":
                try:
                    bracket = stack.pop()
                    if bracket != "[":
                        return False
                except:
                    return False

            elif char == "}":
                try:
                    bracket = stack.pop()
                    if bracket != "{":
                        return False
                except:
                    return False

        if not stack:
            return True
        else:
            return False
