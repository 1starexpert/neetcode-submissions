class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums[i] == target - nums[j]

        """
        num_map = {}
        solution = []
        for i in range(len(nums)):
            if target - nums[i] in num_map:
                solution.append(num_map[target-nums[i]])
                solution.append(i)
    
            num_map[nums[i]] = i
 
        return solution
