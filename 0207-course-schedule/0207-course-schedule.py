class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course):
            nonlocal cycle_set, course_set, graph

            if course in cycle_set:
                return False
            if course in course_set:
                return True
            
            cycle_set.add(course)

            for course_explore in graph[course]:
                if not dfs(course_explore):
                    return False
            course_set.add(course)
            cycle_set.remove(course)

            return True

        cycle_set, course_set = set(), set()
        
        graph = {course: [] for course in range(numCourses)}

        for pre_req, course in prerequisites:
            graph[pre_req].append(course)


        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True