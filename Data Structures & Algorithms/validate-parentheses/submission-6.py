class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")" : "(", "}" : "{", "]" : "["}

        for char in s:
            if char in mapping and stack:
                top_char = stack.pop()
                if mapping[char] != top_char:
                    return False
            else:
                stack.append(char)
            

        return len(stack) == 0