class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = collections.Counter(nums)

        maxheap = []

        for num, frequency in counter_dict.items():
            heapq.heappush(maxheap, (-frequency, num))

        res = []
        while k > 0:
            _, num = heapq.heappop(maxheap)
            res.append(num)
            k -= 1
        return res
