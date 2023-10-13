a=int(input())
n=list(map(int,input().split()))
s=0
m=0
for i in n:
    if(i%2==0):
        s=s+i
    elif(i%2!=0):
        m=m+i
b=abs(m-s)
print(b)