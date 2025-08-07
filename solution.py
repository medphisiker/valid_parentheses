class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        opening_brackets = set(mapping.values())  # множество {'(', '[', '{'}
        
        for char in s:
            if char in opening_brackets:  # O(1) - проверка в множестве
                stack.append(char)
            elif char in mapping:  # O(1) - проверка ключей словаря
                if not stack or stack.pop() != mapping[char]:
                    return False
        
        return not stack