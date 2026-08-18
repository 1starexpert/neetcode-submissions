class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n = 10
        9 -> 10  (1 ways)
        8 -> 10 (2 ways)

        so how many ways to get to 8?
        how many ways to get to 9?

        """
        one = 1
        two = 1
        
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one