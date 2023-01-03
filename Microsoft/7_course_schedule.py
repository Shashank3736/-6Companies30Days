# Leetcode 207: Course Schedule
# https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        def helper(i, visited, path, graph):
            if visited[i] == 1:
                return True
            if visited[i] == 2:
                return False
            visited[i] = 2
            for j in graph[i]:
                if not helper(j, visited, path, graph):
                    return False
            visited[i] = 1
            path.append(i)
            return True
        graph = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            graph[i].append(j)
        visited = [0] * numCourses
        path = []
        for i in range(numCourses):
            if not helper(i, visited, path, graph):
                return False
        return True