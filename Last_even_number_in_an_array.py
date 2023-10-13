a=int(input())
n=list(map(int,input().split()))
s=0
for i in n:
    if(i%2==0):
        s=i
print(s)