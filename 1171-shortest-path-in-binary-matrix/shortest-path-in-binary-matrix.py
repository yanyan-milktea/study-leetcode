from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)

        # if start cell or the end cell is blocked, return -1
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]

        queue = deque([(0, 0, 1)]) #(x, y, cells)
        visited = {(0, 0)}

        while queue:
            x, y, cells = queue.popleft()
            if x == n - 1 and y == n - 1:
                return cells

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if ( 0 <= nx < n and 0 <= ny < n
                and (nx, ny) not in visited
                and grid[nx][ny] == 0):
                    visited.add((nx, ny))
                    queue.append((nx, ny, cells + 1))
        
        return -1

        