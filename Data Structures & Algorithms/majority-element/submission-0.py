class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = {}
        for n in nums:
            if n in num_count:
                num_count[n] += 1
            else:
                num_count[n] = 1
        for key in num_count.keys():
            if num_count[key] > (len(nums) // 2):
                return key
        