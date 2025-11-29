class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dfs(node, time):
            nonlocal updated_time_graph, node_time_graph

            if time >= updated_time_graph[node]:
                return

            updated_time_graph[node] = time
            for nei, w in node_time_graph[node]:
                dfs(nei, time + w)

            return

        node_time_graph = collections.defaultdict(list)
        for u, v, w in times:
            node_time_graph[u].append((v, w))

        updated_time_graph = {node: float("inf") for node in range(1, n + 1)}

        dfs(k, 0)

        res = max(updated_time_graph.values())

        return res if res != float("inf") else -1