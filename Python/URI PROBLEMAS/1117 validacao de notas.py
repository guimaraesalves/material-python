media = 0
qtd = 0
while qtd < 2:
    nota = float(input())
    if(nota >= 0 and nota <= 10):
        media += nota
        qtd += 1
    else:
        print("nota invalida")

print("media = %.2f" %(media/2))