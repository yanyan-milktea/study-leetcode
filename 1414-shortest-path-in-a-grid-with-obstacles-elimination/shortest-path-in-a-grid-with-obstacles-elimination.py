from collections import deque

class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        queue = deque([(0, 0, k, 0)]) # (r, c, k, steps)
        visited = {(0, 0, k)}

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c, remain, steps = queue.popleft()
            if r == m - 1 and c == n - 1:
                return steps
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < m and 0 <= nc < n:
                    new_remain = remain - grid[nr][nc]
                    if new_remain >= 0 and (nr, nc, new_remain) not in visited:
                        visited.add((nr, nc, new_remain))
                        queue.append((nr, nc, new_remain, steps + 1))

        return -1