class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = collections.Counter(nums)
        maxheap = []
        for num, freq in countmap.items():
            heapq.heappush(maxheap, (-freq, num))

        res = []
        for _ in range(k):
            _, num = heapq.heappop(maxheap)
            res.append(num)
        return res