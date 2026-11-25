from collections import deque

class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        if k >= m + n - 2:
            return m + n - 2

        queue = deque([(0, 0, k, 0)]) # (row, col, remain, steps)
        visited = {(0, 0, k)} # (row, col, remain)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            row, col, remain, steps = queue.popleft()
            if row == m - 1 and col == n - 1:
                return steps
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nk = remain - grid[nr][nc]
                    if nk >= 0 and (nr, nc, nk) not in visited:
                        visited.add((nr, nc, nk))
                        queue.append((nr, nc, nk, steps + 1))

        return -1


        