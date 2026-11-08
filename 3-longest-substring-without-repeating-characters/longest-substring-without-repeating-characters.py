class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        res = 0

        for right in range(len(s)):
            curr = s[right]
            while curr in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(curr)
            res = max(res, right - left + 1)

        return res
            
        