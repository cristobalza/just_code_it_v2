class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """

        arr := List[int]
        k := int
        threshold := int

        Number of subarrays of size k and average >= treshold


        arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
                        l.  r

        brute force: iterate through each index per index (nested) O(N2)
        sliding window: O(N * k)

        kadene

        """

        window = sum(arr[:k])
        l = 0
        r = k - 1

        res = 0

        calculate_average = lambda window_value, k=k:  window_value / k

        while r < len(arr):

            if calculate_average(window) >= threshold:
                res += 1 
            
            window -= arr[l]
            l += 1
            if r + 1 < len(arr):
                window += arr[r + 1]
            r += 1

        return res
        


        