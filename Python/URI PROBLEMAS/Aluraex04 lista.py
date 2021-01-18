#Faça um programa utilizando um dict que leia dados de entrada do usuário. O usuário deve entrar
#com os dados de uma pessoa como nome, idade e cidade onde mora (fique livre para acrescentar
#outros). Após isso, você deve imprimir os dados como o exemplo abaixo:
#nome: João
#dade: 20
#idade: São Paulo

#(Opcional) Utilize o exercício anterior e adicione a pessoa em uma lista. Pergunte ao usuário se ele
#deseja adicionar uma nova pessoa. Após adicionar dados de algumas pessoas, você deve imprimir
#todos os dados de cada pessoa de forma organizada.


dados = dict(nome=input("Digite o seu nome: "), idade=input("Idade: "), cidade=input("Cidade: "))
lista = []

adiciona = str(input('Deseja adicionar os dados na lista?\n s - sim\n n - não\n').strip().lower())

adiciona = True
if adiciona == True:

        for adiciona in range(1, 2):
            dados = dict(nome=input("Digite o seu nome: "), idade=input("Idade: "), cidade=input("Cidade: "))



            lista.append(dados)

            lista = lista + lista



#print(dados)
print(lista)