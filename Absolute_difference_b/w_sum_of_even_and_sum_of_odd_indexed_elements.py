a=int(input())
n=list(map(int,input().split()))
s=0
m=0
for i in range(len(n)):
    if(i%2==0):
        s=s+n[i]
    elif(i%2!=0):
        m=m+n[i]
d=abs(s-m)
print(d)