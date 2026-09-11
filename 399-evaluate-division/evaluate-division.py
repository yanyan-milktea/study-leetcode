from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # 1. Build Graph
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        # 2. Define DFS
        def dfs(curr, target, product, visited):
            if curr == target:
                return product

            visited.add(curr)

            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    result = dfs(
                        neighbor,
                        target,
                        product * weight,
                        visited
                    )

                    if result != -1.0:
                        return result

            return -1.0

        # 3. Process queries
        answers = []

        for start, end in queries:
            if start not in graph or end not in graph:
                answers.append(-1.0)
            else:
                result = dfs(start, end, 1.0, set())
                answers.append(result)

        return answers

        