a=int(input())
n=list(map(int,input().split()))
b,c=map(int,input().split())
s=0
for i in range(len(n)):
    if(n[i]<b or n[i]>c):
        s=s+n[i]
print(s)