class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def dfs(node, prev):

            if node in visited:
                return False
            
            visited.add(node)

            for neigh in graph[node]:
                if neigh == prev:
                    continue

                if not dfs(neigh, node):
                    return False

            return True

        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        return  True if dfs(0, None) and len(visited) == n else False