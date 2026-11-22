from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        sr, sc = entrance
        queue = deque([(sr, sc, 0)])
        visited = {(sr, sc)}

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c, steps = queue.popleft()
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if (0 <= nr < m and 0 <= nc < n 
                    and (nr, nc) not in visited 
                    and maze[nr][nc] == '.'):
                    if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                        return steps + 1
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))

        return -1

