class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
         l       m    r
        [4,5,6,0,1,2,3] 
        target = 0
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                # we are in left portion of array
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # nums[m] < nums[r]
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
                
        