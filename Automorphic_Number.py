import math
a=int(input())
b=a*a
c=int(math.log10(a)+1)
f=b%int(10**c)
if(f==a):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")