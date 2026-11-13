from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        r, c = entrance
        queue = deque([(r, c, 0)]) # row, col, steps
        visited = {(r, c)}

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, steps = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < m and 0 <= nc < n
                    and (nr, nc) not in visited
                    and maze[nr][nc] != '+'):
                    if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                        return steps + 1
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))

        return -1




        