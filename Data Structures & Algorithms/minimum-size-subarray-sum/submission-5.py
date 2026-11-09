class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] < target:
                return 0
            else:
                return 1
        

        l = 0
        r = 1
        running_total = nums[l] + nums[r]
        sub_length = 2
        valid_length = 0
        min_length = 0 



        while l < len(nums) and r < len(nums):
            if running_total >= target and min_length != 0:
                min_length = min(sub_length, min_length)
            if running_total >= target and min_length == 0:
                min_length = sub_length
            if nums[l] >= target or nums[r] >= target:
                return 1
            if running_total < target and r < len(nums) - 1:
                r += 1
                running_total += nums[r]
                sub_length += 1
            else:
                running_total -= nums[l]
                l += 1
                sub_length -= 1

        return min_length
                




        