class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []

        potions.sort()

        max_potion = potions[len(potions) - 1]

        for spell in spells:

            min_potion = (success + spell - 1) // spell

            if min_potion > max_potion:
                res.append(0)
            else:
                idx = bisect.bisect_left(potions, min_potion)

                res.append(len(potions) - idx)

        return res

        