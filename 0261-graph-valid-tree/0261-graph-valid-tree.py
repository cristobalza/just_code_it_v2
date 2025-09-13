class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def dfs(node, parent):
            nonlocal visited, graph

            if node in visited or node == parent:
                return False

            visited.add(node)

            for neigh in graph[node]:
                if neigh != parent and not dfs(neigh, node):
                    return False

            return True

        graph = {node: [] for node in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        return dfs(0, None) and len(visited) == n