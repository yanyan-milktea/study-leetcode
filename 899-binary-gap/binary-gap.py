class Solution:
    def binaryGap(self, n: int) -> int:
        prev = -1
        res = 0
        i = 0

        while n > 0:
            if n & 1:
                if prev != -1:
                    res = max(res, i - prev)
                prev = i

            n >>= 1
            i += 1
        
        return res
        