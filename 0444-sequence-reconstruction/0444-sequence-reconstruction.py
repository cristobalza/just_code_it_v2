class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        """
        Given
            nums - supersequence
                n - lenght on nums [1, n]
            sequences - 2d int array where each sequence[i] is a subsequence of nums


        Check if nums is the shortes and the only supersequence on the sequence 2d array
        - shortest supersequence - is a sequence w shortest lenght
        - All of sequences[i] are subsequences of nums

        for sequences = [[1,2],[1,3]] -> [1, 2, 3] or [1,3,2]

        Input: nums = [1,2,3], sequences = [[1,2],[1,3]]

        Chekck if the unique values in sequenece == nums
            set() == nums
        Check if the pair are consecutively match the nums
            for i in range(n - 1):
                if (nums[i], nums[i + 1]) not in pairs:
                    return False
        }

        """

        nums_set = set() # Check if All of sequences[i] are subsequences of nums
        pairs_set = set() # Check shortest supersequence - is a sequence w shortest lenght

        for seq in sequences:
            for i in range(len(seq) - 1):
                nums_set.add(seq[i])
                pairs_set.add((seq[i], seq[i+1]))
            nums_set.add(seq[-1])

        if nums_set != set(nums):
            return False

        for i in range(len(nums) - 1):
            if (nums[i], nums[i + 1]) not in pairs_set:
                return False

        return True


        