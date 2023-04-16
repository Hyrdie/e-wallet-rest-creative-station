import sys

class SudokuBoard:
    def __init__(self):
        self.board = [[0 for x in range(9)] for y in range(9)]
    
    def load_board(self, file_path):
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                for i in range(9):
                    row = lines[i].strip()
                    for j in range(9):
                        self.board[i][j] = int(row[j])
        except:
            print("Error loading board from file")
    
    def add_number(self, row, col, num):
        if self.is_valid_move(row, col, num):
            self.board[row][col] = num
            return True
        else:
            return False
    
    def is_valid_move(self, row, col, num):
        # Check row and column for conflicts
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        # Check subgrid for conflicts
        sub_row = (row // 3) * 3
        sub_col = (col // 3) * 3
        for i in range(sub_row, sub_row + 3):
            for j in range(sub_col, sub_col + 3):
                if self.board[i][j] == num:
                    return False
        return True
    
    def clear_board(self):
        self.board = [[0 for x in range(9)] for y in range(9)]
    
    def draw_board(self):
        print("-------------------------")
        for i in range(9):
            row = "| "
            for j in range(9):
                row += str(self.board[i][j]) + " "
                if j % 3 == 2:
                    row += "| "
            print(row)
            if i % 3 == 2:
                print("-------------------------")
    
def main():
    board = SudokuBoard()
    while True:
        command = input("Enter a command (L, A, R, C, or Q): ").strip().upper()
        if command == "L":
            file_path = input("Enter the path to the board file: ").strip()
            board.load_board(file_path)
            board.draw_board()
        elif command == "A":
            coords = input("Enter the row, column, and number separated by commas: ").strip()
            try:
                row, col, num = [int(x) for x in coords.split(",")]
                if board.add_number(row-1, col-1, num):
                    board.draw_board()
                else:
                    print("Invalid move")
            except:
                print("Invalid input")
        elif command == "R":
            board.draw_board()
        elif command == "C":
            board.clear_board()
        elif command == "Q":
            sys.exit()
        else:
            print("Invalid command")
    
if __name__ == "__main__":
    main()