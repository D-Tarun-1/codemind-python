import math
a=int(input())
len=int(math.log10(a)+1)
sq=int(a**2)
c=int(sq%(10**len))
if(c==a):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")