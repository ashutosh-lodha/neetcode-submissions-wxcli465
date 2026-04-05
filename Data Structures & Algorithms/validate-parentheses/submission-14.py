class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closetoopen={
            "]":"[",
            "}":"{",
            ")":"("
        }
        for char in s:
            if char in closetoopen:
                if stack and stack[-1]==closetoopen[char]:
                    stack.pop()
                else: return False
            else:
                stack.append(char)
        return True if not stack else False

        