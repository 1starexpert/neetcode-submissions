class Solution:
    import math

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Brute force:
        O(n * m) time...

        Binary search over times:
        O(n * log(m)) time... 

        ______
        [1,4,3,2]        10 hours
        """
        l = 1
        r = max(piles)
        possible_min = None
        while l <= r:
            mid = (l + r) // 2
            total_time = 0
            actual_time = 0
            
            for number in piles:
                total_time += math.ceil(number / mid)
                
            


            if total_time > h:
                l = mid + 1
            if total_time < h:
                possible_min = mid
                r = mid - 1
            if total_time == h:
                possible_min = mid
                
                r = mid - 1
                
        return possible_min  




        