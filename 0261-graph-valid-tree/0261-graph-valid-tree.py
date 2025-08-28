class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def dfs(curr, prev):

            if curr in cycle_set or curr == prev:
                return False

            cycle_set.add(curr)

            for preq in graph[curr]:
                if preq != prev and not dfs(preq, curr):
                    return False
            
            return True

        cycle_set = set()

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        return dfs(0, -1) and len(cycle_set) == n 
