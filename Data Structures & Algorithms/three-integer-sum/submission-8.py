class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        nums[i] + nums[j] == -nums[k]
        -nums[i] - nums[j] == nums[k]
        (nums[i] + nums[j]) == -nums[k]
        [-4, -1, -1, 0, 1, 2]
        """
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # try to find a new pair:
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


        


        