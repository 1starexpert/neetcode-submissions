class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        brute force approach:
        """
        l = 0
        r = k - 1

        solution_array = []

        while r < len(nums):
            max_number = nums[l]
            for i in range(l, r + 1):
                if nums[i] > max_number:
                    max_number = nums[i]
            solution_array.append(max_number)
            r += 1
            l += 1
        return solution_array


        