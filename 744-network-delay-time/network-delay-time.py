import heapq
from collections import defaultdict 

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]
        visited = set()
        res = 0

        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            res = time

            for neighbor, w in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (time + w, neighbor))

        return res if len(visited) == n else -1 



