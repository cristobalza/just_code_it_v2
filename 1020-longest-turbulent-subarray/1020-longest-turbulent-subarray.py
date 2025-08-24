class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """

        given: arr
        R: the lenght of max size of a -turbulent- subarray

        turbulent :=  -comparison sign flips- b/n each adjacent pai of elements
                         -> 

          > > <  > < = > >
         0 1 2 3  4 5 6 7 8
        [9,4,2,10,7,8,8,1,9]
                    |
        

        sliding window O(N)/ kadane's algorithm O(N)

        iterate through the array
            register the sign
            compare with previous sign
            if different and not = then +1
            compare with response and check for max value

        """

        res = 1

        l, r = 0, 1

        sign = ""
        
        while r < len(arr):
            
            if arr[r - 1] > arr[r] and sign != ">":
                res = max(res, r - l + 1)
                r += 1
                sign = ">"

            elif arr[r - 1] < arr[r] and sign != "<":
                res = max(res, r - l + 1)
                r += 1
                sign = "<"

            else:
                r = r + 1 if arr[r - 1] == arr[r] else r
                l = r - 1
                sign = ""
        
        return res


        