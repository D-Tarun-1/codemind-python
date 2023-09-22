def prime(n):
    if(n==1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True
import math
a=int(input())
k=int(math.log10(a)+1)
t=a
flag=0
while(a!=0):
    r=a%10
    a//=10
    if(prime(r)):
        flag+=1
if(flag==k):
    if(prime(t)):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")