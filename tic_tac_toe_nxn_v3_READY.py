from tkinter import *

root = Tk()
root.title('Tic Tac Toe')

my_frame = Frame(root, width=500, height=500)
my_frame.pack(fill=BOTH, expand=1)


n = 3
sign_count = 0

button_list = []

win_dict = {}
for num in range(0, n*n):
    win_dict[num] = str(num)


def do_nothing():
    pass


def reset_board():
    global button_list

    button_list = []
    for num in range(0, n*n):
        win_dict[num] = str(num)

    for widget in my_frame.winfo_children():
        widget.destroy()

    construct_buttons()


def popup_click():
    reset_board()
    top.destroy()


def popup(winner):
    global top
    top = Toplevel()
    top.title('WINNER')

    if winner == "draw":
        Label(top, text=" It's a draw", font=("Helvetica", 20), padx=30, pady=30).pack()
    else:
        Label(top, text=win_dict[winner] + " has won. ", font=("Helvetica", 20), padx=30, pady=30).pack()

    Button(top, text="reset game", command=popup_click).pack()

    # disable buttons after popup
    for btn in button_list:
        btn.config(command=do_nothing)


def get_sign():
    global sign_count
    if sign_count % 2 == 0:
        sign_count += 1
        return "O"
    else:
        sign_count += 1
        return "X"


def win_check():
    winner = False
    # check for winners in columns
    for i in range(0, n):
        win_count = 0
        for j in range(0, len(button_list), n):
            if win_dict[i] == win_dict[j+i]:
                win_count += 1
        if win_count == n:
            popup(i)
            winner = True

    # check for winners in rows
    for i in range(0, len(button_list), n):
        win_count = 0
        for j in range(0, n):
            if win_dict[i] == win_dict[j+i]:
                win_count += 1
        if win_count == n:
            popup(i)
            winner = True

    # check for winners in diagonal \
    win_count = 0
    for i in range(0, n):
        if win_dict[0] == win_dict[i+i*n]:
            win_count += 1
    if win_count == n:
        popup(0)
        winner = True

    # check for winners in diagonal /
    win_count = 0
    for i in range(0, n):
        if win_dict[n*n-n] == win_dict[n*(n-i-1)+i]:
            win_count += 1
    if win_count == n:
        popup(n*n-n)
        winner = True

    draw_count = 0
    for btn in button_list:
        if btn['text'] == "O" or btn['text'] == "X":
            draw_count += 1
    if draw_count == n*n and winner is False:
        popup("draw")


def my_click(button_number):
    global button_list

    for index, value in enumerate(button_list):
        if index == button_number:
            value.config(text=get_sign(), command=do_nothing)

    get_sign()
    if get_sign() == "O":
        win_dict[button_number] = "O"
    else:
        win_dict[button_number] = "X"

    win_check()


def construct_buttons():
    for x in range(0, n*n):
        btn = Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50, command=lambda x=x: my_click(x))
        button_list.append(btn)

    grid_count = 0
    for y in range(0, n):
        for z in range(0, n):
            button_list[grid_count].grid(row=y, column=z)
            grid_count += 1


construct_buttons()

root.mainloop()
