import tkinter as tk
from tkinter import messagebox
screen = tk.Tk()
screen.config(bg="white")
screen.geometry("300x400")
screen.title("Tic Tac Toe")
turn = "X"
turns = 0

 
def TicTacToe(button_id):
    global turn,turns
    button_id.config(text=turn)
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    turn_Label.config(text="Turn: "+ turn)
    button_id.config(state=tk.DISABLED)
    if b1.cget("text") == b2.cget("text") == b3.cget("text") != "":
        messagebox.showinfo("You Won!",turn + "won the game!")
b1 = tk.Button(text="",width=13,height=6,bg="black",fg="white",command=lambda: TicTacToe(b1))
b1.place(x=0,y=0)

b2 = tk.Button(text="",width=13,height=6,bg="black",fg="white",command=lambda: TicTacToe(b2))
b2.place(x=100,y=0)

b3 = tk.Button(text="",width=13,height=6,bg="black",fg="white",command=lambda: TicTacToe(b3))
b3.place(x=200,y=0)

b4 = tk.Button(text="",width=13,height=6,bg="black",fg="white",command=lambda: TicTacToe(b4))
b4.place(x=0,y=100)

b5 = tk.Button(text="",width=13,height=6,bg="black",fg="white",command=lambda: TicTacToe(b5))
b5.place(x=100,y=100)

b6 = tk.Button(text="",width=13,height=6,bg="black",fg="white",command=lambda: TicTacToe(b6))
b6.place(x=200,y=100)

b7 = tk.Button(text="",width=13,height=6,bg="black",fg="white",command=lambda: TicTacToe(b7))
b7.place(x=0,y=200)

b8 = tk.Button(text="",width=13,height=6,bg="black",fg="white",command=lambda: TicTacToe(b8))
b8.place(x=100,y=200)

b9 = tk.Button(text="",width=13,height=6,bg="black",fg="white",command=lambda: TicTacToe(b9))
b9.place(x=200,y=200)

turn_Label = tk.Label(text="Turn:"+ turn, width=15,height=1,bg="green",font=("Arial", 12))
turn_Label.place(x=50,y=350)
screen.mainloop()