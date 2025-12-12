class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # TARJAN ALGORITHM
        adj = [[] for _ in range(n)]
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
        
        disc = [-1] * n  # discovery time
        low = [-1] * n   # lowest reachable discovery time
        time = [0]
        res = []
        
        def dfs(node, parent):
            disc[node] = low[node] = time[0]
            time[0] += 1
            
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if disc[neighbor] == -1:  # unvisited
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    # Bridge condition: no back edge from subtree
                    if low[neighbor] > disc[node]:
                        res.append([node, neighbor])
                else:
                    # Back edge found
                    low[node] = min(low[node], disc[neighbor])
        
        dfs(0, -1)
        return res