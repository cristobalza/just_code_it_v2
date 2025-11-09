class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        """
        Given numCourses and prerequisites, return true if can finish the coursers

        adj. List
        0 []
        1 [0]


        check for 0
        {0, 1}
        -> [1]
            X
            check for 1 and 
            True
        {1, 0}

        same size of numCourses

        backtracing approach

        base case: if it is in the cycle (False) or has been visited (True)
        mark candidate: add to the cycle check
        explore: iterate through the prerequisites
        remove candidate: rm from cycle and add to the visited
        
        return True
        """

        def backtrack(course, cycle):

            if course in cycle:
                return False

            if course in visited:
                return True
            
            cycle.add(course)

            for prereq in graph[course]:
                if not backtrack(prereq, cycle):
                    return False

            cycle.remove(course)
            visited.add(course)

            return True

        graph = {course: [] for course in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)

        visited = set()

        for course in range(numCourses):
            if not backtrack(course, set()):
                return False

        return True if len(visited) == numCourses else False