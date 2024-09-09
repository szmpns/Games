import random
import tkinter as tk

window = tk.Tk()

window.title("Tic Tac Toe")

def quit_game():
    window.destroy()

def reset_game():
    global player

    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
            buttons[row][col].config(bg="#F0F0F0")

def empty_spaces():

    spaces = 9

    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def check_winner():

    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            buttons[0][col].config(bg="green")
            buttons[1][col].config(bg="green")
            buttons[2][col].config(bg="green")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif empty_spaces() is False:
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(bg="yellow")
        return "Tie"
    else:
        return False


def next_turn(row, col):
    global player

    if buttons[row][col]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][col]["text"] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
            elif check_winner() == "Tie":
                label.config(text=("Tie"))
        else:
            buttons[row][col]["text"] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
            elif check_winner() == "Tie":
                label.config(text=("Tie"))



players = ["X" , "O"]

player = random.choice(players)


buttons = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

frame = tk.Frame(window)
frame.grid()

label2 = tk.Button(text="reset",font=("consolas" , 40) , command= lambda : reset_game())
label2.grid()

label = tk.Label(text=player + " turn" , font=("consolas" , 40))
label.grid()

label3 = tk.Button(text="Quit" , font=("consolas" , 40) , command= lambda : quit_game())
label3.grid()

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(frame , text="" , font=("consolas" , 40) , width=5 , height=2, command=lambda row=row , col=col : next_turn(row , col))
        buttons[row][col].grid(row=row , column=col)




window.mainloop()