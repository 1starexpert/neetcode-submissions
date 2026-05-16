class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## try brute force solution:    
        bestArea = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                area = min(heights[i], heights[j]) * abs(j - i)
                #print(area)
                if area > bestArea:
                    bestArea = area
        return bestArea

        