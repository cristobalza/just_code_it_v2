class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def backtrack(course, cycled):
            nonlocal visited, graph

            if course in visited:
                return True

            if course in cycled:
                return False

            cycled.add(course)

            for prereq in graph[course]:
                if not backtrack(prereq, cycled):
                    return False

            cycled.remove(course)
            visited.add(course)

            return True

        
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        visited = set()

        for course in range(numCourses):
            if course in graph:
                if not backtrack(course, set()):
                    return False

        return True