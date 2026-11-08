from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        res = 0

        for ch in set(count_s) | set(count_t):
            res += abs(count_s[ch] - count_t[ch])

        return res      