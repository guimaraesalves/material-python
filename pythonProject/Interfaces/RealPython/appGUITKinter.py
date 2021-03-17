import tkinter as tk

window = tk.Tk()
label = tk.Label(
    text="Olá Mundo!",
    fg="White", # Set the text color to white 
    bg="#34A2FE",  # Set the background color to black
    width=10,
    height=10,
    
    )

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
label.pack()
button.pack()
window.mainloop()

