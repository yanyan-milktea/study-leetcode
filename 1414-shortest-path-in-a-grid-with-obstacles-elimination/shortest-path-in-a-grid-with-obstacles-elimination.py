from collections import deque
class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        if k >= m + n - 2:
            return m + n - 2

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(0, 0, k, 0)]) # (r, c, remains, steps)
        visited = {(0, 0, k)} #(r, c, remains)

        while queue:
            r, c, remains, steps = queue.popleft()
            if r == m - 1 and c == n - 1:
                return steps
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < m and 0 <= nc < n):
                    new_remain = remains - grid[nr][nc]
                    if (new_remain >= 0 and (nr, nc, new_remain) not in visited):
                        visited.add((nr, nc, new_remain))
                        queue.append((nr, nc, new_remain, steps + 1))

        return -1