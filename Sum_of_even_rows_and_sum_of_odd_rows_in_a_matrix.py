a,b=map(int,input().split())
ls=[]
s=0
s1=0
for i in range(a):
    lt=list(map(int,input().split()))[:b:]
    ls.append(lt)
for i in range(0,a):
    if(i%2==0):
        s+=sum(ls[i])
    else:
        s1+=sum(ls[i])
print(s,s1)