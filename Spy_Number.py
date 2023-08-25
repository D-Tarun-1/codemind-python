a=int(input())
s=0
p=1
while(a>0):
    d=a%10
    s=s+d
    p=p*d
    a=a//10
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")