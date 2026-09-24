class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = collections.deque()
        res = []
        completed = 0

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            res.append(course)
            completed += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return res if completed == numCourses else []
        