#!/usr/bin/env python
# IMPORTA O tkinter e cria uma nova janela
import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

window = tk.Tk()
window.title("Conversor de Temperatura") # tiulo na barra da janela


frm_entry = tk.Frame(master=window)# frm_entry é um contêiner que agrupa ent_temperaturee lbl_tempune.

ent_temperature = tk.Entry(master=frm_entry, width=10) # Entrywidget para entrar com o valor
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}") # escreve °F depois da caixa


ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w") 
#lbl_tempser colocado diretamente à direita de ent_temperature.Você configurou o stickyparâmetro para "e"para ent_temperaturepara que ele sempre fique na extremidade direita da célula da grade. Você também define stickycomo "w"para lbl_tempmantê-lo preso à extremidade esquerda da célula da grade. Isso garante que lbl_tempesteja sempre localizado imediatamente à direita de ent_temperature.


# faça o btn_converte o lbl_resultpara converter a temperatura inserida ent_temperaturee exibir os resultados
btn_convert = tk.Button(
    master=window,
    text="-->",
    command=fahrenheit_to_celsius
)

lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

 #frm_entry, btn_converte lbl_resultsão atribuídos a window. Juntos, esses três widgets formam as três células na grade principal do aplicativo. Use .grid()para ir em frente e apresentá-los agora:

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)




window.mainloop()