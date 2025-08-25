class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        numbers := List[int]
        - 1 indexed array
        - sorted in non-decreasing order (asc)

        R: find 2 nums s.t. they add up to target. Return the indi


         numbers = [2,7,11,15], target = 9
                    l r

                    numbers[l] + numbers[r] = 9
        
        """

        l, r = 0, len(numbers) - 1


        while l < r:
            while l < r and numbers[l] + numbers[r] > target:
                r -= 1
            
            while l < r and numbers[l] + numbers[r] < target:
                l += 1
        
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

