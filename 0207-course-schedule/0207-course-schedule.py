class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_visit_set = set()

        def dfs(course, course_cycle_set):
            nonlocal course_visit_set

            if course in course_cycle_set:
                return False

            if course in course_visit_set:
                return True

            course_cycle_set.add(course)

            for next_course in graph[course]:
                if not dfs(next_course, course_cycle_set):
                    return False
            
            course_cycle_set.remove(course)
            course_visit_set.add(course)

            return True

        graph = {course_num : [] for course_num in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)

        for course in range(numCourses):
            if not dfs(course, set()):
                return False
        return True
        