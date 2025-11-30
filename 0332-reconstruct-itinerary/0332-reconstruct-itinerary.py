class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        - This problem asks for an **Eulerian path** (visit every edge exactly once)
        - We use a greedy DFS that takes the smallest lexicographic option first
        - By adding airports in **postorder** (after exhausting all neighbors), we build the path backwards
        - Sorting in reverse and using `pop()` gives us O(1) removal instead of O(n)

        **Time Complexity:** O(E log E) where E is the number of tickets (for sorting)
        **Space Complexity:** O(E) for the graph and recursion
        """
        # Build graph with sorted destinations (in reverse for efficient pop)
        graph = collections.defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        
        # Sort in reverse order so we can pop from the end
        for src in graph:
            graph[src].sort(reverse=True)
        
        result = []
        
        def dfs(airport):
            # Visit all outgoing edges first
            while graph[airport]:
                next_airport = graph[airport].pop()  # O(1) pop from end
                dfs(next_airport)
            # Add to result in postorder (after visiting all neighbors)
            result.append(airport)
        
        dfs("JFK")
        
        # Reverse because we built it backwards
        return result[::-1]
