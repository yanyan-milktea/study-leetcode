class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # 1. Get rows and columns
        rows = len(grid)
        cols = len(grid[0])

        # 2. Add all rotten oranges to the queue
        #    and count fresh oranges
        queue = collections.deque()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        # 3. Multi-source BFS
        #    Each level represents one minute
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        while queue and fresh > 0:
            level = len(queue)

            for _ in range(level):
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if ( 0 <= new_row < rows
                        and 0 <= new_col < cols
                        and grid[new_row][new_col] == 1):

                        grid[new_row][new_col] = 2
                        fresh -= 1
                        queue.append((new_row, new_col))
                
            minutes += 1


        # 4. Return the result
        #    If fresh oranges remain, return -1
        return minutes if fresh == 0 else -1