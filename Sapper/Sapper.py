import tkinter as tk
import random

window = tk.Tk()
window.title("Sapper")

# Game params
rows, cols = 10, 10
num_bombs = 15

bombs_data = [[0 for _ in range(cols)] for _ in range(rows)]
buttons = [[None for _ in range(cols)] for _ in range(rows)]
revealed = [[False for _ in range(cols)] for _ in range(rows)]

bombs_to_place = num_bombs
while bombs_to_place > 0:
    r = random.randint(0, rows - 1)
    c = random.randint(0, cols - 1)
    if bombs_data[r][c] == 0:
        bombs_data[r][c] = 1
        bombs_to_place -= 1

def check_bombs(row, col):
    counter = 0
    for r in range(max(0, row - 1), min(row + 2, rows)):
        for c in range(max(0, col - 1), min(col + 2, cols)):
            if r == row and c == col:
                continue
            if bombs_data[r][c] == 1:
                counter += 1
    return counter

def check_win():
    for i in range(rows):
        for j in range(cols):
            if bombs_data[i][j] == 0 and not revealed[i][j]:
                return False
    return True

def still_playing():
    for i in range(rows):
        for j in range(cols):
            buttons[i][j].config(state=tk.DISABLED)

def reveal_cells(row, col):
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return
    if revealed[row][col]:
        return
    
    revealed[row][col] = True
    count = check_bombs(row, col)
    buttons[row][col].config(text=str(count) if count > 0 else " ", state=tk.DISABLED, bg="grey")
    
    if count == 0:
        for r in range(max(0, row - 1), min(row + 2, rows)):
            for c in range(max(0, col - 1), min(col + 2, cols)):
                if r != row or c != col:
                    reveal_cells(r, c)

def next_turn(row, col):
    if bombs_data[row][col] == 0:
        reveal_cells(row, col)
        if check_win():
            label = tk.Label(frame, text="You won!", font=("Arial", 20), fg="green")
            label.grid(row=rows, column=0, columnspan=cols)
            still_playing()
    else:
        buttons[row][col].config(text="💣", fg="red")
        label = tk.Label(frame, text="You lost!", font=("Arial", 20), fg="red")
        label.grid(row=rows, column=0, columnspan=cols)
        still_playing()

def toggle_flag(row, col):
    if not revealed[row][col]:
        if buttons[row][col]['text'] == "🚩":
            buttons[row][col].config(text=" ")
        else:
            buttons[row][col].config(text="🚩")

frame = tk.Frame(window)
frame.grid()

for i in range(rows):
    for j in range(cols):
        buttons[i][j] = tk.Button(frame, text=" ", font=("Arial", 20), width=3, height=1, command=lambda i=i, j=j: next_turn(i, j))
        buttons[i][j].bind("<Button-3>", lambda event, i=i, j=j: toggle_flag(i, j))
        buttons[i][j].grid(row=i, column=j)

window.mainloop()