from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.title('Tic Tac Toe')
root.geometry("420x420")

my_frame = Frame(root, width=500, height=500)
my_frame.pack(fill=BOTH, expand=1)


n = 3
click_count = 0
sign_count = 0

button_list = []

win_dict = {}
for num in range(0, n*n):
    win_dict[num] = str(num)


def reset_board():
    global button_list

    button_list = []
    for num in range(0, n*n):
        win_dict[num] = str(num)

    for widget in my_frame.winfo_children():
        widget.destroy()

    construct_buttons()


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

    # disable buttons
    # for index, value in enumerate(button_list):
    #     print(index, value, win_dict[index])
    #     y = index // n
    #     z = index % n
    #     new_btn = f'Button(my_frame, text="{win_dict[index]}", font=("Helvetica", 32), padx=55, pady=50)'
    #     eval(f'{new_btn}.grid(row={y}, column={z})')



def get_sign():
    global sign_count
    if sign_count % 2 == 0:
        sign_count += 1
        return "O"
    else:
        sign_count += 1
        return "X"


def win_check():

    draw_count = 0
    # check for winners in columns
    for i in range(0, n):
        win_count = 0
        for j in range(0, len(button_list), n):
            if win_dict[i] == win_dict[j+i]:
                win_count += 1
        if win_count == n:
            popup(i)
        elif click_count == n*n:
            draw_count += 1

    # check for winners in rows
    for i in range(0, len(button_list), n):
        win_count = 0
        for j in range(0, n):
            if win_dict[i] == win_dict[j+i]:
                win_count += 1
        if win_count == n:
            popup(i)
        elif click_count == n*n:
            draw_count += 1

    # check for winners in diagonals \
    win_count = 0
    for i in range(0, n):
        if win_dict[0] == win_dict[i+i*n]:
            win_count += 1
    if win_count == n:
        popup(0)
    elif click_count == n * n:
        draw_count += 1

    # check for winners in diagonals / ERRORS
    win_count = 0
    for i in range(0, n):
        if win_dict[n*n-n] == win_dict[n*n-2*n+1]:
            win_count += 1
    if win_count == n:
        popup(n*n-n)
    elif click_count == n * n:
        draw_count += 1

    if draw_count == 4:
        popup("draw")


def my_click(button_number):
    global click_count
    click_count += 1

    for index, value in enumerate(button_list):
        if index == button_number:
            y = index // n
            z = index % n
            new_btn = 'Button(my_frame, text=get_sign(), font=("Helvetica", 32), padx=55, pady=50)'
            eval(f'{new_btn}.grid(row={y}, column={z})')

    get_sign()
    if get_sign() == "O":
        win_dict[button_number] = "O"
    else:
        win_dict[button_number] = "X"

    win_check()


def construct_buttons():
    for x in range(0, n*n):
        btn = f'Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda: my_click({x}))'
        button_list.append(btn)

    grid_count = 0
    for y in range(0, n):
        for z in range(0, n):
            eval(f'{button_list[grid_count]}.grid(row={y}, column={z})')
            # getattr(button_list[counter], f'grid(row={y}, column={z})')
            grid_count += 1


construct_buttons()

root.mainloop()
