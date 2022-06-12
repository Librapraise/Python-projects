def find_next_empty_space(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none) 
    
    #keep in mind that we are using 0-8 four indices

    for r in range(9):
        for c in range(9): # range (9) is 0, 1, 2,. ... 8
            if puzzle[r][c] == -1:
                return r, c

    return None, None #if no spaces in the puzzle to make a guess

def is_valid(puzzle, guess, row, col):
    #figures out whether the guess at the row/col of the puzzle is a valid guess
    #returns True if is valid, False otherwise

    # start with the row:
    row_val = puzzle[row]
    if guess in row_val:
        return False
    
    # for the column
    col_val = [puzzle[i][col] for i in range(9)]
    if guess in col_val:
        return False
    
    #and then the square
    # might be tricky, we want to get where the 3x3 square starts
    # and iterate over the 3 values in the row/column
    row_starter = (row // 3) * 3 #dividing by 3 and rounding up
    col_starter = (col // 3) * 3 

    for r in range(row_starter, row_starter + 3):
        for c in range(col_starter, col_starter + 3):
            if puzzle[r][c] == guess:
                return False
    return True


def solve_sudoku(puzzle):
    # solve sudoku using a backtracking technique
    # our puzzle is a list of lists, where each inner list is arow in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)

    # step 1: choose somewhere on the puzzle tomake a guess
    row, col = find_next_empty_space(puzzle)

    #step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True
    
    #step 2: if there's is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range (1, 10) is 1, 2, 3, ... 9
        #step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this valid, then place that guess on the puzzle
            puzzle[row][col] = guess
            # now recurse using this puzzle
            #step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
        #step 5: if not valid OR if the guess does not solve the puzzle, then we need to...
        #...backtrack and try a new number
        puzzle[row][col] = -1  # reset the guess
    
    #step 6: if none of the numbers that we try works, then this puzzle is UNSOLVABLE
    return False

if __name__== '__main__':
    sample_board = [
        [3, 9, -1,  -1, 5, -1,  -1, -1, -1],
        [-1, -1, -1,  2, -1, -1,  -1, -1, -1],
        [-1, -1, -1,  7, 1, 9,  -1, 8, -1],

        [-1, 5, -1,  -1, 6, 8,  -1, -1, -1],
        [2, -1, 6,  -1, -1, 3,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, 4],

        [5, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [6, 7, -1,  1, -1, 5,  -1, 4, -1],
        [1, -1, 9,  -1, -1, -1,  2, -1, -1]
    ]
    print(solve_sudoku(sample_board))
    print(sample_board)
