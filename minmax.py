import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("AI Tic-Tac-Toe")
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        # Create 3x3 grid of buttons
        for i in range(9):
            btn = tk.Button(self.window, text="", font=('normal', 20, 'bold'), 
                            height=3, width=6, command=lambda i=i: self.user_click(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def analyzeboard(self, b):
        cb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in range(8):
            if b[cb[i][0]] != 0 and b[cb[i][0]] == b[cb[i][1]] == b[cb[i][2]]:
                return b[cb[i][2]]
        return 0

    def minimax(self, board, player):
        x = self.analyzeboard(board)
        if x != 0: return x * player
        pos, value = -1, -2
        for i in range(9):
            if board[i] == 0:
                board[i] = player
                score = -self.minimax(board, player * -1)
                board[i] = 0
                if score > value:
                    value, pos = score, i
        return 0 if pos == -1 else value

    def comp_turn(self):
        pos, value = -1, -2
        for i in range(9):
            if self.board[i] == 0:
                self.board[i] = 1
                score = -self.minimax(self.board, -1)
                self.board[i] = 0
                if score > value:
                    value, pos = score, i
        if pos != -1:
            self.update_board(pos, 1)

    def user_click(self, i):
        if self.board[i] == 0:
            self.update_board(i, -1)
            if self.analyzeboard(self.board) == 0 and 0 in self.board:
                self.comp_turn()
            self.check_game_over()

    def update_board(self, i, player):
        self.board[i] = player
        self.buttons[i].config(text="X" if player == -1 else "O", state="disabled", disabledforeground="black")

    def check_game_over(self):
        res = self.analyzeboard(self.board)
        if res == -1:
            messagebox.showinfo("Result", "X Wins!")
            self.window.quit()
        elif res == 1:
            messagebox.showinfo("Result", "O Wins (Computer)!")
            self.window.quit()
        elif 0 not in self.board:
            messagebox.showinfo("Result", "It's a Draw!")
            self.window.quit()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()