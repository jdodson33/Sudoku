# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 18:16:51 2023

@author: dodsonj
"""


class SudokuSolver:
    def __init__(self):
        self.board = []

    def sudokuSolver(self):
        # Solution 2: backtracking
        find = self.findEmpty(self.board)
        if not find:
            return True
        else:
            row, col = find
        # print(board)
        for i in range(1, 10):
            if self.isValid(self.board, i, (row, col)):
                self.board[row][col] = i

                if self.sudokuSolver():
                    return True

                self.board[row][col] = 0

        return False

    def printBoard(self, mat):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("---------------------")

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")

                if j == 8:
                    print(str(mat[i][j]))
                else:
                    print(str(mat[i][j]) + " ", end="")

    def findEmpty(self, mat):
        for i in range(9):
            for j in range(9):
                if int(mat[i][j]) == 0:
                    return i, j  # (row, col)
        return None

    def isValid(self, mat, num, pos):
        # check row
        for i in range(9):
            if int(mat[pos[0]][i]) == num and pos[1] != i:
                return False

        # check col
        for j in range(9):
            if int(mat[j][pos[1]]) == num and pos[0] != j:
                return False

        # check 3x3
        box_x, box_y = pos[1] // 3, pos[0] // 3
        for i in range(box_y * 3, (box_y * 3) + 3):
            for j in range(box_x * 3, (box_x * 3) + 3):
                if int(mat[i][j]) == num and (i, j) != pos:
                    return False

        return True


board = [["5", "3", "0", "0", "7", "0", "0", "0", "0"],
         ["6", "0", "0", "1", "9", "5", "0", "0", "0"],
         ["0", "9", "8", "0", "0", "0", "0", "6", "0"],
         ["8", "0", "0", "0", "6", "0", "0", "0", "3"],
         ["4", "0", "0", "8", "0", "3", "0", "0", "1"],
         ["7", "0", "0", "0", "2", "0", "0", "0", "6"],
         ["0", "6", "0", "0", "0", "0", "2", "8", "0"],
         ["0", "0", "0", "4", "1", "9", "0", "0", "5"],
         ["0", "0", "0", "0", "8", "0", "0", "7", "9"]]

board2 = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
          [0, 1, 0, 0, 0, 4, 0, 0, 0],
          [4, 0, 7, 0, 0, 0, 2, 0, 8],
          [0, 0, 5, 2, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 9, 8, 1, 0, 0],
          [0, 4, 0, 0, 0, 3, 0, 0, 0],
          [0, 0, 0, 3, 6, 0, 0, 7, 2],
          [0, 7, 0, 0, 0, 0, 0, 0, 3],
          [9, 0, 3, 0, 0, 0, 6, 0, 4]]

result = SudokuSolver()
result.board = board2
print(result.printBoard(result.board))
result.sudokuSolver()
print(result.printBoard(result.board))


