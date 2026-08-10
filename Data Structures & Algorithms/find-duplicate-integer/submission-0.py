class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        This employs floyd algorithm
        """

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # now slow gives us the location of the intersection point
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        