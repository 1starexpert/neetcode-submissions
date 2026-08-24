class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        for i in range(len(nums)):
            num_set[nums[i]] = i
        print(num_set)
        for i in range(len(nums)):
            missing = target - nums[i]
            if missing in num_set:
                if i == num_set[missing]:
                    continue
                sol_arr = [i, num_set[missing]]
                return sol_arr


                


        