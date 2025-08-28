class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(curr_course, prev_course, cycle_set):

            if curr_course is None or curr_course in visited:
                return True

            if curr_course == prev_course or curr_course in cycle_set:
                return False

            cycle_set.add(curr_course)

            for prev in graph[curr_course]:
                if not dfs(prev, graph.get(prev, None), cycle_set):
                    return False

            cycle_set.remove(curr_course)
            visited.add(curr_course)

            return True

        graph = collections.defaultdict(list)
        for a, b, in prerequisites:
            graph[a].append(b)

        visited = set()
        for course in range(numCourses):
            if course in graph:
                if not dfs(course, None, set()):
                    return False

        return True
        