a=int(input())
n=list(map(int,input().split()))
c=0
for i in range(1,a-1):
    if((n[i-1]%2!=0) and (n[i+1]%2!=0) and (n[i]%2==0)):
        c+=1
print(c)