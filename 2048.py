from tkinter import *
from random import *

root = Tk()
root.wm_title("2048")

top = Frame(root)
top.pack()

db_2048 = {"size": 4, "top": top, "begin_with": "2"}
db_2048["board"] = board = []

colors = (
    "#fcefe6", "#f2e8cb", "#f5b682", "#f29446", "#ff775c", "#e64c2e", 
    "#ede291", "#fce130", "#ffdb4a", "#f0b922", "#fad74d"
)
size = len(colors)
i = int(db_2048["begin_with"])
for j in range(size):
    db_2048[str(i)] = colors[j]
    i *= 2

f = Frame(db_2048["top"], bg="gray")
f.pack(padx=20, pady=20)

s = db_2048["size"]
for r in range(s):
    row_list = []
    for c in range(s):
        l = Label(f, text=" ", bg="white", width=6, height=3)
        row_list.append(l)
        l.grid(row=r, column=c, padx=1, pady=1)
    board.append(row_list)

move_panel = Frame(db_2048["top"])
move_panel.pack(side="left")

Label(move_panel, text=" ", width=3).grid(row=0, column=0)
db_2048["^"] = b = Button(move_panel, text="^", width=3,
                          command=lambda: squeeze_up())
b.grid(row=0, column=1)
Label(move_panel, text=" ", width=3).grid(row=0, column=2)

db_2048["<"] = b = Button(move_panel, text="<", width=3,
                          command=lambda: squeeze_left())
b.grid(row=1, column=0)
Label(move_panel, text=" ", width=3).grid(row=1, column=1)
db_2048[">"] = b = Button(move_panel, text=">", width=3,
                          command=lambda: squeeze_right())
b.grid(row=1, column=2)

Label(move_panel, text=" ", width=3).grid(row=2, column=0)
db_2048["v"] = b = Button(move_panel, text="v", width=3,
                          command=lambda: squeeze_down())
b.grid(row=2, column=1)
Label(move_panel, text=" ", width=3).grid(row=2, column=2)

# add padding
Label(db_2048["top"], text=" ", width=3).pack(side="left")
db_2048["restart"] = b = Button(db_2048["top"], text="New Game",
                                fg="DeepPink1", command=lambda: new_game())
b.pack(side="left")


def new_game():
    s = db_2048["size"]
    b = db_2048["board"]
    for r in range(s):
        for c in range(s):
            l = b[r][c]
            l["text"] = " "
            l["bg"] = "white"
    add_new()
    add_new()


def add_new():
    s = db_2048["size"]
    b = db_2048["board"]
    possible = []
    for r in range(s):
        for c in range(s):
            l = b[r][c]
            if l["text"] == " ": possible.append(l)
    choice = len(possible) * random()
    l = possible[int(choice)]
    l["text"] = db_2048["begin_with"]
    l["bg"] = db_2048[db_2048["begin_with"]]


def squeeze_right():
    s = db_2048["size"]
    for k in range(1, s):  # start from 1, go thru 3 times
        for r in range(s):
            for c in range(s - 1, 0, -1):
                try_move(r, c - 1, r, c)
    set_color()
    add_new()


def squeeze_left():
    s = db_2048["size"]
    for k in range(1, s):  # start from 1, so we go thru 3 times
        for r in range(s):
            for c in range(s - 1):
                try_move(r, c + 1, r, c)
    set_color()
    add_new()


def squeeze_down():
    s = db_2048["size"]
    for k in range(1, s):  # start from 1, so we go thru 3 times
        for c in range(s):
            for r in range(s - 1, 0, -1):
                try_move(r - 1, c, r, c)
    set_color()
    add_new()


def squeeze_up():
    s = db_2048["size"]
    for k in range(1, s):  # start from 1, so we go thru 3 times
        for c in range(s):
            for r in range(s - 1):
                try_move(r + 1, c, r, c)
    set_color()
    add_new()


def set_color():
    s = db_2048["size"]
    b = db_2048["board"]
    for r in range(s):
        for c in range(s):
            l = b[r][c]
            t = l["text"]
            if t == " ":
                l["bg"] = "white"
            else:
                l["bg"] = db_2048[t]


def try_move(from_r, from_c, to_r, to_c):
    b = db_2048["board"]
    if b[to_r][to_c]["text"] == " ":
        b[to_r][to_c]["text"] = b[from_r][from_c]["text"]
        b[from_r][from_c]["text"] = " "
        return
    if b[to_r][to_c]["text"] == b[from_r][from_c]["text"]:
        n = int(b[to_r][to_c]["text"])
        b[to_r][to_c]["text"] = str(n * 2)
        b[from_r][from_c]["text"] = " "
        return
    return  # (from_r, from_c) cannot move into (to_r, to_c)


root.wm_resizable(0, 0)
root.mainloop()
