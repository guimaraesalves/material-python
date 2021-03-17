# Descrição: um programa em python GUI for a chat bot

# Biblioteca
from tkinter import *

storage_adapter="chatterbot.storage.MongoDatabaseAdapter"
from chatterbot import ChatBot

# Uncomment the following lines to enable verbose logging
import logging
logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='mongodb://localhost:27017/chatterbot-database'
)

print('Hello World!! Olá Mundo vamos conversar...')

while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break


#Criando o objeto tK do tkinter
root = Tk()

# Colocando o titulo da janela
root.title('Chat Bot Hank')

# Inserindo o tamanho da janela ou Geometria
root.geometry('400x500')

#Create a main menu bar
main_menu = Menu(root)

#Create submenu
file_menu = Menu(root)
file_menu.add_command(label='Novo', font=('ubuntu'))
file_menu.add_command(label='Salvar como', font=('ubuntu'))
file_menu.add_command(label='Sair', font=('ubuntu'))


main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_command(label='Edit')
main_menu.add_command(label='Quit')
root.config(menu=main_menu)

#Create the chat window
chatWindow = Text(root, bd=1, bg='black', width=50, height=0)
chatWindow.place(x=6, y=6, height=385, width=370)

#Create tk message window
messageWindow = Text(root, bg='black', width=30, height=4,)
messageWindow.place(x=128, y=400, height=88, width=260)

#Create a button to send the message the message
Button = Button(root, text='ENVIAR', bg='blue', activebackground='light blue', width=12, height=5, font=('ubuntu', 20))
Button.place(x=6, y=400, height=88, width=120)

#Add a scroll bar
scrollbar = Scrollbar(root, command=chatWindow.yview())
scrollbar.place(x=375, y=5, height=385)

root.mainloop()
