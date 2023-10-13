a=int(input())
num=list(map(int,input().split()))
c=0
for i in range(1,a-1):
    if((num[i+1]%2!=0) and (num[i-1]%2==0) or (num[i+1]%2==0) and (num[i-1]%2!=0)):
        c+=1
print(c)