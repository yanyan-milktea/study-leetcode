class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start):
            if len(path) == k:
                res.append(path[:])
                return

            # At most (n - i + 1) numbers remain from i onward.
            # We need (k - len(path)) more. So stop early if not enough remain.
            need = k - len(path)
            # The pruning bound n - need + 2 comes from: 
            # the last valid start is n - need + 1 (leaving exactly need numbers), 
            # so the range endpoint is n - need + 2. 
            # For k=2, n=4 at an empty path, that's range(1, 4) — correct. 4 -(2-0)+2 = 4
            for i in range(start, n - need + 2):
                path.append(i)
                dfs(i + 1)
                path.pop()

        dfs(1)
        return res

