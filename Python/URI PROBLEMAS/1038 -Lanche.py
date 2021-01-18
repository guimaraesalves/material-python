preco = input().split()
cod, qtd = preco
qtd = int(qtd)
tabela = {"1":4.0, "2":4.5, "3":5.0, "4":2.0, "5":1.5}

total = qtd * tabela[cod]

print('Total: R$ %.2f' %total)
