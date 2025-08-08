class Solution:
    def isValid(self, s: str) -> bool:
        # если число символов в строке нечетное, точно есть
        # скобка без пары, строка со скобками не валидная
        if len(s) % 2 != 0:
            return False
        
        stack = []
        mapping = {")":"(", "]":"[", "}":"{"}
        open_brackets = set(mapping.values())
        
        for char in s:
            # операция O(1) для множества
            if char in open_brackets: 
                stack.append(char)

            # операция O(1) для словаря (хэш таблицы)
            elif not stack or stack.pop() != mapping[char]:
                return False
        
        return not stack