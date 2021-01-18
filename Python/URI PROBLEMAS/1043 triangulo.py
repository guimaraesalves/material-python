val = input().split()
a, b, c = val

a = float(a)
b = float(b)
c = float(c)

if a < (a+b) and b < (c+a) and c < (a+b):
    per = a + b + c
    print('Area = %.2f' %per)
