def palin(n):
    s=0
    d=n
    while(n!=0):
        r=n%10
        s=s*10+r
        n//=10
    if(d==s):
        print("True")
    else:
        print("False")
a=int(input())
for i in range(a):
   # b=int(input())
    c=int(input())
    palin(c)