class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        # two distinct number
        while l < r:
            curr = numbers[l] + numbers[r]
            if curr == target:
                # 1-indexed 
                return [l + 1, r + 1]
            elif curr < target:
                l += 1
            else:
                r -= 1
        