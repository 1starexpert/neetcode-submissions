class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]

        target=13
        """
        row_left = 0
        row_right = len(matrix) - 1

        while row_right >= row_left:
            row_middle = (row_right + row_left) // 2

            l = 0
            r = len(matrix[row_middle]) - 1

            last_num = None
            while l <= r:
                
                mid = (r + l) // 2
                print(f"l={l}, mid={mid}, r={r}")
                last_num = matrix[row_middle][mid]
                if matrix[row_middle][mid] > target:
                    r = mid - 1
                if matrix[row_middle][mid] < target:
                    l = mid + 1
                if matrix[row_middle][mid] == target:
                    return True

            if target > last_num:
                row_left = row_middle + 1
            if target < last_num:
                row_right = row_middle - 1

        return False
                



        