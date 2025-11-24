# sudoku
makes sudoku answers
currently my code outputs a 2d array of fully filled in 9x9 sudokus

use: 'makeOneSudoku()' to make one filled out sudoku

use: 'makeManySudokus(amount)' to make many sudokus

example usage:

import sudoku

num = input("how many sudokus should I create: ")

sudokus = makeManySudokus(num)

for sudoku in sudokus:
    print(sudoku)
