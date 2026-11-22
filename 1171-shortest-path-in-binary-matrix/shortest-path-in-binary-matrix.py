from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        queue = deque([(0, 0, 1)]) #(r, c, cells)
        visited = {(0, 0)}

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while queue:
            r, c, cells = queue.popleft()
            if r == n - 1 and c == n - 1:
                return cells

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if (0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc, cells + 1))

        return -1
        