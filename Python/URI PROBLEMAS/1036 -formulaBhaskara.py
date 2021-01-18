import math
num = input().split()
a , b , c = num

a = float(a)
b = float(b)
c = float (c)

x1 = 0
x2 = 0

x = (b**2)-(4*a*c)


if(x <0) or (a==0):
     print('Impossivel calcular')
else:
     x=math.sqrt(x)
     x1 = (-b+x)/(2*a)
     x2 = (-b-x)/(2*a)
     print("R1 = %.5f\nR2 = %.5f" %(x1,x2))
