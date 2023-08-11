import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
d=(s*(s-a)*(s-b)*(s-c))
v=math.sqrt(d)
print(f"{v:.2f}")