class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s: return s
        s = list(s)

        # Get rid of extra ')'
        left = 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            elif s[i] == ')':
                if left > 0:
                    left -= 1
                else:
                    s[i] = ""

        # Get rid of extra '('
        right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                right += 1
            elif s[i] == '(':
                if right > 0:
                    right -= 1
                else:
                    s[i] = ""

        return "".join(s)
        