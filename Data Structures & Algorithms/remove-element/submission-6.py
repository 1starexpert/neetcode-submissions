class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
 
            if nums[r] == val:
                r -= 1
            if nums[l] != val:
                l += 1
            if nums[l] == val and nums[r] != val and l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1
        counter = 0
        for i in range(len(nums)):
            if nums[i] != val:
                counter += 1

        return counter


        