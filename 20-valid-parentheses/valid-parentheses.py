class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"(" : ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char in hashmap:
                stack.append(char)
            else:
                if stack and hashmap[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
        