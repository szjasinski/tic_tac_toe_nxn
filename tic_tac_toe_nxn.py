import tkinter as tk


class TicTacToe(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        my_frame = tk.Frame(parent)
        n = 4
        sign_count = 0
        coord_button_dict = {}
        coord_sign_dict = {}
        top = tk.Toplevel()

        def do_nothing():
            pass

        def reset_board():
            nonlocal coord_button_dict
            nonlocal coord_sign_dict
            nonlocal sign_count

            coord_button_dict.clear()
            coord_sign_dict.clear()
            sign_count = 0

            for widget in my_frame.winfo_children():
                widget.destroy()

            construct_buttons()

        def popup_click():
            reset_board()
            top.destroy()

        def popup(winner):
            nonlocal top
            top = tk.Toplevel()
            top.title('WINNER')

            if winner == "draw":
                tk.Label(top, text=" It's a draw", font=("Helvetica", 20), padx=30, pady=30).pack()
            else:
                tk.Label(top, text=winner + " has won. ", font=("Helvetica", 20), padx=30, pady=30).pack()

            tk.Button(top, text="reset game", command=popup_click).pack()

            # disable buttons after popup
            for coords in coord_button_dict:
                coord_button_dict[coords].config(command=do_nothing)

        def get_sign():
            nonlocal sign_count
            if sign_count % 2 == 0:
                sign_count += 1
                return "O"
            else:
                sign_count += 1
                return "X"

        def are_items_equal(my_list):
            count = 0
            for item in my_list:
                if item == my_list[0]:
                    count += 1
            if count == len(my_list):
                return True
            else:
                return False

        def win_check():
            is_draw = True

            # check for winner in rows(x) and columns(y)
            count_coord = 0
            while count_coord < n:
                win_list_x = []
                win_list_y = []
                for coords in coord_sign_dict:
                    if coords[0] == count_coord:
                        win_list_x.append(coord_sign_dict[coords])
                    if coords[1] == count_coord:
                        win_list_y.append(coord_sign_dict[coords])
                count_coord += 1

                if len(win_list_x) == n and are_items_equal(win_list_x):
                    popup(win_list_x[0])
                    is_draw = False
                elif len(win_list_y) == n and are_items_equal(win_list_y):
                    popup(win_list_y[0])
                    is_draw = False

            # check for winner in diagonals
            win_list_diag1 = []
            win_list_diag2 = []
            for coords in coord_sign_dict:
                if coords[0] == coords[1]:
                    win_list_diag1.append(coord_sign_dict[coords])
                if coords[0] + coords[1] == n - 1:
                    win_list_diag2.append(coord_sign_dict[coords])

            if len(win_list_diag1) == n and are_items_equal(win_list_diag1):
                popup(win_list_diag1[0])
                is_draw = False
            elif len(win_list_diag2) == n and are_items_equal(win_list_diag2):
                popup(win_list_diag2[0])
                is_draw = False

            # check for a draw
            if len(coord_sign_dict) == n * n and is_draw:
                popup("draw")

        def my_click(x, y):
            for coords in coord_button_dict:
                if coords[0] == x and coords[1] == y:
                    coord_button_dict[coords].config(text=get_sign(), command=do_nothing)

            get_sign()
            if get_sign() == "O":
                coord_sign_dict[(x, y)] = "O"
            else:
                coord_sign_dict[(x, y)] = "X"

            win_check()

        def construct_buttons():
            grid_count = 0
            for x in range(0, n):
                for y in range(0, n):
                    btn = tk.Button(my_frame, text="  ", font=("Helvetica", 32), padx=55, pady=50,
                                    command=lambda x=x, y=y: my_click(x, y))
                    coord_button_dict[(x, y)] = btn
                    coord_button_dict[(x, y)].grid(row=x, column=y)
                    grid_count += 1

        construct_buttons()
        my_frame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title('TIC TAC TOE')
    TicTacToe(root).pack()
    root.mainloop()
