class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        row  =   [set() for i in range(9)]
        cols =  [set() for i in range(9)]
        boxes =  [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] !=".":
                    nums = int(board[i][j])
                    row[i].add(nums)
                    cols[j].add(nums)
                    box_id = i // 3 * 3 + j//3
                    boxes[box_id].add(nums)
        def backtrack(i,j):
            nonlocal solved
            if i== 9 :
                solved = True
                return 
            new_i = i+ (j+1)//9
            new_j = (j+1)%9
            if board[i][j] !=".":
                backtrack(new_i,new_j)
            else:
                for num in range(1,10):
                    box_id = i // 3 * 3 + j//3
                    if num  not in row[i] and num  not in cols[j] and num not in boxes[box_id]:
                        row[i].add(num)
                        cols[j].add(num)
                        boxes[box_id].add(num)
                        board[i][j] = str(num)
                        backtrack(new_i,new_j)
                        if not solved:
                            row[i].remove(num)
                            cols[j].remove(num)
                            boxes[box_id].remove(num)
                            board[i][j] = "."
        solved = False
        backtrack(0,0)
        print(board)

board =[["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
solve = Solution()
solve.solveSudoku(board)

