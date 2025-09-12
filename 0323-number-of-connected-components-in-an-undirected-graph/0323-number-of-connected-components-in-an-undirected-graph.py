class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(node):
            nonlocal visited, graph

            if node in visited:
                return 

            visited.add(node)

            for neigh in graph[node]:
                dfs(neigh)

            return


        graph = {num : [] for num in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        res = 0

        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node)

        return res
