class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prefix and suffix method:
        pre: 
        [1, 2, 8, 48]

        """
        pre_arr = []
        post_arr = []
        sol_arr = []
        rev = nums[::-1]

        for i in range(len(nums)):
            if i == 0:
                pre_arr.append(nums[i])
            else:
                pre_arr.append(pre_arr[i - 1] * nums[i])
        

        for i in range(len(nums)):
            if i == 0:
                post_arr.append(rev[i])
            else:
                post_arr.append(rev[i] * post_arr[i - 1])
        post_arr.reverse()

        for i in range(len(nums)):
            if i == 0:
                sol_arr.append(post_arr[i + 1])
            elif i == len(nums) - 1:
                sol_arr.append(pre_arr[i - 1])
            else:
                sol_arr.append(pre_arr[i - 1] * post_arr[i + 1])
        return sol_arr