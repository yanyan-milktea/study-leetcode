class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0

        for _ in range(k + 1):           # at most k+1 edges
            prev = dist[:]               # ⚠️ key：copy，don't change
            for u, v, w in flights:
                if prev[u] < INF:
                    dist[v] = min(dist[v], prev[u] + w)

        return dist[dst] if dist[dst] < INF else -1