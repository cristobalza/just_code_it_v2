class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Input: nums = [1,2,3]

        all subsets have n size
        no dups

        backtrack approach

        edg case: subset reach same size of nums

        mark candidate: do a permutation with next value

        explore: call recursively to i + 1

        remove candidate: do the same permutation 


        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

        """

        def backtrack(i, subset):
            if i == len(subset):
                res.append(subset.copy())
                return

            for j in range(i, len(nums)):
                subset[i], subset[j] = subset[j], subset[i]

                backtrack(i+1, subset)

                subset[i], subset[j] = subset[j], subset[i]
            
            return 

        res = []
        backtrack(0, nums)
        return res