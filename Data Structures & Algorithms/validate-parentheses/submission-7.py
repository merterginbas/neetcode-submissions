class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        isOpen={")":"(", "]" : "[", "}":"{" }
        for c in s:
            if c in isOpen:
                if stack and stack[-1] == isOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False