class Solution:
    def reorganizeString(self, s: str) -> str:
        count_hmap = {}
        for ch in s:
            count_hmap[ch] = 1 + count_hmap.get(ch, 0)

        max_heap = [(-freq, ch) for ch, freq in count_hmap.items()]
        heapq.heapify(max_heap) # O(N)

        prev = None
        res = ""

        while max_heap or prev:
            if prev and not max_heap:
                return ""

            freq, ch = heapq.heappop(max_heap)
            freq += 1 # add so it shrinks
            res += ch

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if freq != 0:
                prev = (freq, ch)

        return res
