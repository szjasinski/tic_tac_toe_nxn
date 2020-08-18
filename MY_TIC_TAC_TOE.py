from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.title('Tic Tac Toe')
root.geometry("420x420")

my_frame = Frame(root, width=500, height=500)
my_frame.pack(fill=BOTH, expand=1)


count = 0
win_dict = {}
for num in range(1, 10):
    win_dict[num] = str(num)


def reset_board():
    for x in range(1, 10):
        win_dict[x] = str(x)

    for widget in my_frame.winfo_children():
        widget.destroy()

    button_1 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(1))
    button_2 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(2))
    button_3 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(3))
    button_4 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(4))
    button_5 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(5))
    button_6 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(6))
    button_7 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(7))
    button_8 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(8))
    button_9 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(9))

    button_1.grid(row=0, column=0)
    button_2.grid(row=0, column=1)
    button_3.grid(row=0, column=2)
    button_4.grid(row=1, column=0)
    button_5.grid(row=1, column=1)
    button_6.grid(row=1, column=2)
    button_7.grid(row=2, column=0)
    button_8.grid(row=2, column=1)
    button_9.grid(row=2, column=2)


def popup_ok():
    reset_board()
    top.destroy()


def popup(winner):
    global top
    top = Toplevel()
    top.title('WINNER')
    top.geometry("150x60")
    if winner == "draw":
        Label(top, text=" It's a draw").pack()
    else:
        Label(top, text=win_dict[winner] + " has won. ").pack()
    Button(top, text="ok", command=popup_ok).pack()


def get_sign():
    global count
    if count % 2 == 0:
        count += 1
        return "O"
    else:
        count += 1
        return "X"


def win_check(button_number):
    global win_dict

    get_sign()
    if get_sign() == "O":
        win_dict[button_number] = "O"
    else:
        win_dict[button_number] = "X"

    if win_dict[1] == win_dict[2] == win_dict[3]:
        popup(1)
    elif win_dict[4] == win_dict[5] == win_dict[6]:
        popup(4)
    elif win_dict[7] == win_dict[8] == win_dict[9]:
        popup(7)
    elif win_dict[1] == win_dict[4] == win_dict[7]:
        popup(1)
    elif win_dict[2] == win_dict[5] == win_dict[8]:
        popup(2)
    elif win_dict[3] == win_dict[6] == win_dict[9]:
        popup(3)
    elif win_dict[1] == win_dict[5] == win_dict[9]:
        popup(1)
    elif win_dict[3] == win_dict[5] == win_dict[7]:
        popup(3)
    elif click_count == 9:
        popup("draw")


click_count = 0
def my_click(button_number):
    global click_count
    global button_1
    global button_2
    global button_3
    global button_4
    global button_5
    global button_6
    global button_7
    global button_8
    global button_9

    click_count += 1

    if button_number == 1:
        button_1 = Button(my_frame, text=get_sign(), font=("Helvetica", 32), padx=55, pady=50)
        button_1.grid(row=0, column=0)
        win_check(button_number)
    elif button_number == 2:
        button_2 = Button(my_frame, text=get_sign(), font=("Helvetica", 32), padx=55, pady=50)
        button_2.grid(row=0, column=1)
        win_check(button_number)
    elif button_number == 3:
        button_3 = Button(my_frame, text=get_sign(), font=("Helvetica", 32), padx=55, pady=50)
        button_3.grid(row=0, column=2)
        win_check(button_number)
    elif button_number == 4:
        button_4 = Button(my_frame, text=get_sign(), font=("Helvetica", 32), padx=55, pady=50)
        button_4.grid(row=1, column=0)
        win_check(button_number)
    elif button_number == 5:
        button_5 = Button(my_frame, text=get_sign(), font=("Helvetica", 32), padx=55, pady=50)
        button_5.grid(row=1, column=1)
        win_check(button_number)
    elif button_number == 6:
        button_6 = Button(my_frame, text=get_sign(), font=("Helvetica", 32), padx=55, pady=50)
        button_6.grid(row=1, column=2)
        win_check(button_number)
    elif button_number == 7:
        button_7 = Button(my_frame, text=get_sign(), font=("Helvetica", 32), padx=55, pady=50)
        button_7.grid(row=2, column=0)
        win_check(button_number)
    elif button_number == 8:
        button_8 = Button(my_frame, text=get_sign(), font=("Helvetica", 32), padx=55, pady=50)
        button_8.grid(row=2, column=1)
        win_check(button_number)
    elif button_number == 9:
        button_9 = Button(my_frame, text=get_sign(), font=("Helvetica", 32), padx=55, pady=50)
        button_9.grid(row=2, column=2)
        win_check(button_number)


button_1 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(1))
button_2 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(2))
button_3 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(3))
button_4 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(4))
button_5 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(5))
button_6 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(6))
button_7 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(7))
button_8 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(8))
button_9 = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click(9))

button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)
button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)



root.mainloop()
