a,b=map(int,input().split())
max1=max(a,b)
for i in range(1,max1+1):
    if(a%i==0 and b%i==0):
        hcf=i
print(hcf)