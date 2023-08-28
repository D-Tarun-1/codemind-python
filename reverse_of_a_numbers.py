a=int(input())
c=0
while(a!=0):
    d=a%10
    c=c*10+d
    a//=10
print(c)