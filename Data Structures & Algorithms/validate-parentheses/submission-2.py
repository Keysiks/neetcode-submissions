class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sl = {"[": "]", "(": ")", "{": "}"}
        for el in s:
            if el in "({[":
                stack.append(el)
            else:
                if len(stack) != 0 and sl[stack[-1]] == el:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0