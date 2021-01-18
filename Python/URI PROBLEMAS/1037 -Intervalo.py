vl = float(input())

fora = True
res = ''

if(vl < 0 or vl > 100):
    res += 'Fora de intervalo'
    fora = False
    
if(vl <= 25.00 and fora):
    res += 'Intervalo [0,25]'
    fora = False

if(vl <= 50.0 and fora):
    res += 'Intervalo (25,50]'
    fora = False
    
if(vl <=75.0 and fora):
    res += 'Intervalo (50,75]'
    fora = False

if(vl <=100.0 and fora):
    res += 'Intervalo (75,100]'
    fora = False

print(res)
