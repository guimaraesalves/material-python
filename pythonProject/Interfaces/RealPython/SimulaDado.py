import random
import tkinter as tk


def roll():
    lbl_result["text"] = str(random.randint(1, 6))


def roll2():
    lbl_result1["text"] = str(random.randint(1, 6))


window = tk.Tk()
window.columnconfigure([0, 1], minsize=150)
window.rowconfigure([0, 1], minsize=50)

btn_roll = tk.Button(text="Dado 1", command=roll)
lbl_result = tk.Label()

btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0)

btn_roll1 = tk.Button(text="Dado 2", command=roll2)
lbl_result1 = tk.Label()

btn_roll1.grid(row=0, column=1, sticky="nsew")
lbl_result1.grid(row=1, column=1)







window.mainloop()
