meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril','Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
n = 0
while(n < 4):
    mes = int(input("Escolha um mês (1-12): "))
    if 1 <= mes <= 12:
        print('O mês é {}'.format(meses[mes-1]))
    n += 1