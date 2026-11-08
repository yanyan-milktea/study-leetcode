from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)

        left = 0
        valid = 0
        start = 0
        res_len = float("inf")

        for right in range(len(s)):
            in_char = s[right]
            window[in_char] += 1
            if window[in_char] == need[in_char]:
                valid += 1
            
            while valid == len(need):
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    start = left
                out_char = s[left]
                if window[out_char] == need[out_char]:
                    valid -= 1
                window[out_char] -= 1
                left += 1

        return "" if res_len == float("inf") else s[start : start + res_len]
        




        