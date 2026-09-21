class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        # 1. Create result and monotonic stack
        n = len(heights)
        result = [0] * n
        stack = []

        # 2. Traverse from right to left
        for i in range(n - 1, -1, -1):
            visible = 0

        # 3. Count shorter people that are popped
            while stack and heights[i] >= stack[-1]:
                stack.pop()
                visible += 1

        # 4. Count the first taller person, if one remains
            if stack:
                visible += 1

        # 5. Add the current person to the stack
            result[i] = visible
            stack.append(heights[i])

        return result