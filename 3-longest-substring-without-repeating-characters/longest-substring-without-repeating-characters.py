class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLength = 0
        left = 0

        for right in range(len(s)):
            curr = s[right]

            while curr in seen:
                seen.remove(s[left])
                left += 1

            seen.add(curr)
            maxLength = max(maxLength, right - left + 1)

        return maxLength    