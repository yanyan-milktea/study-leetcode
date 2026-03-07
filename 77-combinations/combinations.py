class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                dfs(i + 1)
                path.pop()

        dfs(1)
        return res

