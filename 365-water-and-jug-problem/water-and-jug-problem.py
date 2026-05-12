from collections import deque 
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False

        start = (0, 0)
        q = collections.deque([start])
        visited = {start}
        parent = {start: None}

        while q:
            a, b = q.popleft()

            if a == target or b == target or a + b == target:
                path = []
                curr = (a, b)
                while curr:
                    path.append(curr)
                    curr = parent[curr]
                print (path[::-1])

                return True


            next_step = []

            next_step.append((x, b))
            next_step.append((a, y))
            next_step.append((0, b))
            next_step.append((a, 0))

            pour = min(a, y - b)
            next_step.append((a - pour, b + pour))

            pour = min(b, x - a)
            next_step.append((a + pour, b - pour))

            for nxt in next_step:
                if nxt not in visited:
                    visited.add(nxt)
                    parent[nxt] = (a, b)
                    q.append(nxt)

        return False
