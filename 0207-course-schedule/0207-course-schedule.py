class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(course, cycle):

            if course in visited:
                return True

            if course in cycle:
                return False

            cycle.add(course)

            for prereq in adj[course]:
                if not dfs(prereq, cycle):
                    return False

            cycle.remove(course)
            visited.add(course)

            return True


        adj = {course: [] for course in range(numCourses)}
        # Directed graph
        for a, b in prerequisites:
            adj[a].append(b)

        visited = set()
        for course in range(numCourses):
            if course in visited:
                continue
            else:
                if not dfs(course, set()):
                    return False

        return True if len(visited) == numCourses else False