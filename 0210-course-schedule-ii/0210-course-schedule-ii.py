class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """

        Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]

        adj list:

        course: prerequisites
        0: []
        1: [0]
        2: [0]
        3: [1, 2]


        [0, 1, 2, 3]

        """

        def dfs(course):

            if course in cycle:
                return False

            if course in visited:
                return True



            cycle.add(course)
            
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        graph = collections.defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        res = []
        visited, cycle = set(), set()

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res