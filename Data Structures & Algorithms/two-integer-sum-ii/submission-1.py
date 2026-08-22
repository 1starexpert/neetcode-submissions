class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l = 0
        r = len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1
            if s < target:
                l += 1
            if s == target:
                res.append(l + 1)
                res.append(r + 1)
                break
        return res
        