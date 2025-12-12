class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        """
        n = size of position array
        position - position[i] -> basket

        m = number of balls need to distribute the balls into the baskets st the min force between any two balls is max

        |x - y| difference force

        Given position, m R force

        Input: position = [1,2,3,4,7], m = 3
                           i

        [1 2 3 4 - - 7]
         l.          r
               m

        
    
        """
        position.sort()
        
        def can_place_balls(min_dist):
            count = 1  # Place first ball at position[0]
            last_pos = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_pos >= min_dist:
                    count += 1
                    last_pos = position[i]
                    if count == m:  # Early exit optimization
                        return True
            
            return False
        
        left, right = 1, position[-1] - position[0]
        result = 0
        
        while left <= right:
            mid = left + (right - left) // 2  # Avoid overflow
            
            if can_place_balls(mid):
                result = mid
                left = mid + 1  # Try larger distance
            else:
                right = mid - 1  # Try smaller distance
        
        return result
        