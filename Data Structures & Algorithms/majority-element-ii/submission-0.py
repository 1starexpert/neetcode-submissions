class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for element in nums:
            if element not in count:
                count[element] = 1
            else:
                count[element] += 1
        sol = []
        for key in count.keys():
            if count[key] > len(nums) // 3:
                sol.append(key)
        return sol
        