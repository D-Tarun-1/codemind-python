a=int(input())
b=int(input())
s,r=0,0
for i in range(1,a):
    if(a%i==0):
        s=s+i
for j in range(1,b):
    if(b%j==0):
        r=r+j
if(s==b and r==a):
    print("Amicable")
else:
    print("Not Amicable")