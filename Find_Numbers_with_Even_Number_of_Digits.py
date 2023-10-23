a=int(input())
lst=list(map(str,input().split()))
s=0
for i in lst:
    if(len(i)%2==0):
        s+=1
print(s)