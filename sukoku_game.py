class Sudoku_game: 
    def __init__ (self, board = None):
        if(board == None):
            self.suduko_board = Sudoku_board
        else:
            self.suduko_board = board
    def __str__(self):
        return str(self.suduko_board)

class Sudoku_board:
    def __init__ (self):
        self.board = [[0]*9]*9
    def __str__(self):
        my_str = ""
        for y in range (9):
            for x in range (9):
                my_str += str(self.board[x][y]) + " "
                if((x+1) % 3 == 0):
                    my_str += " "
            my_str += "\n"
            if((y+1) % 3 == 0):
                    my_str += "\n"
        return my_str

my_game = Sudoku_game()

board = Sudoku_board()
print(my_game)