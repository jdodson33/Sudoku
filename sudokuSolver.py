# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 18:16:51 2023

@author: dodsonj
"""

board = [["5","3","0","0","7","0","0","0","0"],
         ["6","0","0","1","9","5","0","0","0"],
         ["0","9","8","0","0","0","0","6","0"],
         ["8","0","0","0","6","0","0","0","3"],
         ["4","0","0","8","0","3","0","0","1"],
         ["7","0","0","0","2","0","0","0","6"],
         ["0","6","0","0","0","0","2","8","0"],
         ["0","0","0","4","1","9","0","0","5"],
         ["0","0","0","0","8","0","0","7","9"]]

board2 = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
          [0, 1, 0, 0, 0, 4, 0, 0, 0],
          [4, 0, 7, 0, 0, 0, 2, 0, 8],
          [0, 0, 5, 2, 0, 0, 0, 0, 0],
    	  [0, 0, 0, 0, 9, 8, 1, 0, 0],
	      [0, 4, 0, 0, 0, 3, 0, 0, 0],
	      [0, 0, 0, 3, 6, 0, 0, 7, 2],
	      [0, 7, 0, 0, 0, 0, 0, 0, 3],
	      [9, 0, 3, 0, 0, 0, 6, 0, 4]]

def sudokuSolver(board):        
    #Solution 2: backtracking
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find
    #print(board)
    for i in range(1, 10):
        if isValid(board, i, (row, col)):
            board[row][col] = i
                
            if sudokuSolver(board):
                return True
                
            board[row][col] = 0
        
    return False

        
        
def printBoard(mat):
    for i in range(9):
        if i%3==0 and i != 0:
            print("---------------------")
                    
        for j in range(9):
            if j%3==0 and j != 0:
                print("| ", end="")
                    
            if j == 8:
                print(str(mat[i][j]))
            else:
                print(str(mat[i][j]) + " ", end="")
    
def findEmpty(mat):
    for i in range(9):
        for j in range(9):
            if int(mat[i][j]) == 0:
                return (i, j) #(row, col)
    return None
    
    
def isValid(mat, num, pos):
    #check row
    for i in range(9):
        if int(mat[pos[0]][i]) == num and pos[1] != i:
            return False
        
    #check col
    for j in range(9):
        if int(mat[j][pos[1]]) == num and pos[0] != j:
            return False
        
    #check 3x3
    box_x, box_y = pos[1]//3, pos[0]//3
    for i in range(box_y*3, (box_y*3)+3):
        for j in range(box_x*3, (box_x*3)+3):
            if int(mat[i][j]) == num and (i, j) != pos:
                return False
    
    return True
                
                
        
        
        

printBoard(board2)
output = sudokuSolver(board2)
print(" ")
printBoard(board2)
    
    
    
    
    
    


        #Brute force solution
        # def scan(x, y):
        #     possib = [x for x in range(1,10)]
        #     for i in range(9): #check the current row for existing #'s
        #         if board[y][i] != ".":
        #             possib.remove(int(board[y][i]))
        #     for j in range(9): #check the current column for existing #'s
        #         if board[j][x] != "." and int(board[j][x]) in possib:
        #             possib.remove(int(board[j][x]))
        #     x_quad, y_quad = x//3, y//3
        #     for m in range(y_quad*3, (y_quad*3)+3): #check in the 3x3 quadrant
        #         for n in range(x_quad*3, (x_quad*3)+3):
        #             if board[m][n] != "." and int(board[m][n]) in possib:
        #                 possib.remove(int(board[m][n]))
        #     return possib

        # go = True

        # while go:
        #     for i in range(9):
        #         for j in range(9):
        #             if board[i][j] == ".":
        #                 go = True
        #                 break
        #             else:
        #                 go = False
        #         if go == True:
        #             break
            
        #     for i in range(9):
        #         for j in range(9):
        #             if board[i][j] == ".":
        #                 pos = scan(j, i)
        #                 if len(pos) == 1:
        #                     board[i][j] = str(pos[0])