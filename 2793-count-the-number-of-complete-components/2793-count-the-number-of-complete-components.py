class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(node, explore_list):

            if node in visited:
                return

            visited.add(node)
            explore_list.append(node)

            for neigh in adj_list[node]:
                dfs(neigh, explore_list)

            return explore_list


        visited, count = set(), 0

        adj_list = collections.defaultdict(list)

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        for node in range(n):
            if node in visited:
                continue
            
            out_explore_list = dfs(node, [])

            size_neigh_nodes = len(out_explore_list) - 1

            if all([size_neigh_nodes == len(adj_list[neigh]) for neigh in out_explore_list]):
                count += 1
            
        return count