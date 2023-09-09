def arium(n):
    l=0
    while(n!=0):
        l=l+1
        n//=10
    return l
a=int(input())
s=0
b=a
c=arium(a)
while(a!=0):
    r=a%10
    s=s+(r**c)
    a//=10
    c=c-1
if(s==b):
    print("True")
else:
    print("False")