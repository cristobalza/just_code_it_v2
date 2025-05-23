class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def backtrack(course, cycle_set):
            nonlocal visited

            if course in visited:
                return True

            if course in cycle_set:
                return False

            cycle_set.add(course)

            for next_course in graph[course]:
                if not backtrack(next_course, cycle_set):
                    return False
            
            cycle_set.remove(course)
            visited.add(course)

            return True

        graph = {node: [] for node in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)

        visited = set()

        for course in range(numCourses):
            if not backtrack(course, set()):
                return False
        
        return True