a=int(input())
b=0
c=1
s=0
print(b,end=' ')
print(c,end=' ')
for i in range(1,a-1):
    s=b+c
    b=c
    c=s
    print(s,end=' ')
    