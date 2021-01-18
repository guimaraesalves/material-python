

idade = int(input())
a = int(idade / 365)
m = int(idade%365/30)
d = int(idade%365%30)

print('%d ano(s)\n%d mes(es)\n%d dia(s)' %(a,m,d))
