notas = input().split()
p1, p2, p3, p4 = notas

p1 = float(p1)
p2 = float(p2)
p3 = float(p3)
p4 = float(p4)

nota_prova = 0.0
MEDIA = ((p1*2)+(p2*3)+(p3*4)+(p4*1))/10

print('Media: %.1f' %MEDIA)

if(MEDIA >= 7.0):
    print("Aluno aprovado.")

if(MEDIA < 5.0):
    print("Aluno reprovado.")

if(MEDIA >= 5.0 and MEDIA <= 6.9):
    print("Aluno em exame.")
    nota_prova = float(input())
    print("Nota do exame: %.1f" %nota_prova)
    MEDIA = (MEDIA + nota_prova)/2
    
    if(MEDIA >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print('Media final: %.1f' %MEDIA)
