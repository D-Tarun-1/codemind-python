a=int(input())
n=list(map(int,input().split()))
b=int(input())
c=0
for i in n:
    if i==b:
        c+=1
print(c)