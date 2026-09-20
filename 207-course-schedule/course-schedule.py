class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # [1, 0] 0 -> 1
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = collections.deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completed = 0
        while queue:
            course = queue.popleft()
            completed += 1
            
            for next_graph in graph[course]:
                indegree[next_graph] -= 1
                if indegree[next_graph] == 0:
                    queue.append(next_graph)

        return completed == numCourses

