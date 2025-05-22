class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def dfs(node, prev_node):
            nonlocal visited

            if node in visited:
                return False

            visited.add(node)

            for children in graph[node]:
                if children != prev_node and not dfs(children, node):
                    return False
            
            return True

        graph = collections.defaultdict(list)

        visited = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        return dfs(0, -1) and len(visited) == n

