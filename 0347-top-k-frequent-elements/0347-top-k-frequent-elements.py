class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_hmap = collections.defaultdict(int)

        for num in nums:
            counter_hmap[num] = -1 + counter_hmap.get(num, 0)

        max_heap = []

        for num, freq in counter_hmap.items():
            heapq.heappush(max_heap, (freq, num))

        res = []
        while k > 0 and max_heap:
            _, num = heapq.heappop(max_heap)

            res.append(num)

            k -= 1

        return res
