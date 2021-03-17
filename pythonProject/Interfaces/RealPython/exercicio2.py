import tkinter as tk

window = tk.Tk()

label = tk.Label(text='Título')
text_box = tk.Text()
entry = tk.Entry()
name = entry.get()

label.pack()
entry.pack()
text_box.pack()




window.mainloop()

