class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        We start off with a brute force solution:
        """

        # check that each row is valid: 
        for i in range(len(board)):
            num_set = set()
            for j in range(9):
                if board[i][j] in num_set and board[i][j] not in ".":
                    print("row")
                    return False
                num_set.add(board[i][j])

        # check that each column is valid:
        for j in range(9):
            num_set = set()
            for i in range(9):
                if board[i][j] in num_set and board[i][j] not in ".":
                    print("column")
                    return False
                num_set.add(board[i][j])

        # check that each box is valid:
        # create a hashset for each box:
        set_arr = []
        for i in range(9):
            set_arr.append(set())

        for i in range(9):
            for j in range(9):
                box_id = int((i // 3) * 3 + (j / 3))
                if board[i][j] not in "." and board[i][j] in set_arr[box_id]:
                    return False
                set_arr[box_id].add(board[i][j])
        return True
            



                
        