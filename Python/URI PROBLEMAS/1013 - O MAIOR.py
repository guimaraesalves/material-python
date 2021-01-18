import math

vlr = input().split(" ")
A, B, C = vlr
M = (int(A) + int(B) + abs(int(A) - int(B)))  / 2
result = (int(M) + int(C) + abs(int(M) - int(C)))/2
print("%d eh o maior" %result)
