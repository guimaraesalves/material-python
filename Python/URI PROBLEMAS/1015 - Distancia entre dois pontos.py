
import math

P1 = input().split(" ")
P2 = input().split(" ")
x1,y1 = P1
x2,y2 = P2
dist = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))
print("%0.4f" %dist)
