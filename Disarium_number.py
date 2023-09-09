def arium(n):
    l=0
    while(n!=0):
        l=l+1
        n//=10
    return l
a=int(input())
s=0
dis=arium(a)
b=a
while(a!=0):
    r=a%10
    s=s+(r**dis)
    a//=10
    dis=dis-1
if(s==b):
    print("True")
else:
    print("False")