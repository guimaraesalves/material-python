import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    # usam a askopenfilenamecaixa de diálogo do tkinter.filedialogmódulo para exibir uma caixa de diálogo de abertura de arquivo e armazenar o caminho do arquivo selecionado filepath.
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    # verificam se o usuário fecha a caixa de diálogo ou clica no botão Cancelar
    if not filepath:
        return
    
    # limpa o conteúdo atual de txt_edituso .delete().
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text) # atribui a string texta ser txt_editusada .insert().
    window.title(f"Simple Text Editor - {filepath}") # define o título da janela de forma que contenha o caminho do arquivo aberto.


def save_file():
    """Save the current file as a new file."""
    # usam a asksaveasfilenamecaixa de diálogo para obter o local de salvamento desejado do usuário. O caminho do arquivo selecionado é armazenado na filepathvariável.
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    # erificam se o usuário fecha a caixa de diálogo ou clica no botão Cancelar 
    if not filepath:
        return
    # cria um novo arquivo no caminho de arquivo selecionado.
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END) # extrai o texto do método txt_editwith .get()e o atribui à variável text.
        output_file.write(text) # grava textno arquivo de saída.
    window.title(f"Simple Text Editor - {filepath}") # atualiza o título da janela para que o novo caminho do arquivo seja exibido no título da janela.


window = tk.Tk()
window.title("Simple Text Editor")

# definem as configurações de linha e coluna.
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


# criam os quatro widgets de que você precisa para a caixa de texto, o quadro e os botões abrir e salvar.
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)


# Essas duas linhas de código criam uma grade com duas linhas e uma coluna no fr_buttonsquadro, uma vez que ambas btn_opene btn_savetêm seus masteratributos definidos como fr_buttons. 
# btn_opené colocado na primeira linha e btn_savena segunda linha para que btn_openapareça acima btn_save no layout
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)


# Essas duas linhas de código criam uma grade com uma linha e duas colunas para window. Você coloca fr_buttonsna primeira coluna e txt_editna segunda coluna de forma que fr_buttons apareça à esquerda txt_edit no layout da janela.
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew") # sticky parâmetro como "nsew", o que o força a se expandir em todas as direções .


window.mainloop()

