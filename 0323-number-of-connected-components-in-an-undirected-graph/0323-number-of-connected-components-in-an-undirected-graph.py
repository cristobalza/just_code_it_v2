class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(node, prev):
            nonlocal visited, graph

            if node in visited:
                return False

            visited.add(node)
            
            for neigh in graph[node]:
                if neigh != prev and neigh not in visited:
                    if not dfs(neigh, node):
                        return False

            return True

        visited = set()
        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        res = 0

        for node in range(n):

            if dfs(node, None):
                res += 1

        return res