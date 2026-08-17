class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        given = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in given:
                if not stack or stack[-1] != given[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack