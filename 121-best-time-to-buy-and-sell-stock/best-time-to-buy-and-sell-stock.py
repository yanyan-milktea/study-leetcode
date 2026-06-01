class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxEarnings = 0

        for price in prices:
            minPrice = min(price, minPrice)
            maxEarnings = max(maxEarnings, price - minPrice)

        return maxEarnings

