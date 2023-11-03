a,b=map(int,input().split())
s=0
s1=0
ls=[]
for i in range(a):
    inner=list(map(int,input().split()))
    ls.append(inner)
for inner in ls:
    for j in inner:
        if j%2==0:
            s=s+j
        else:
            s1=s1+j
print(s,s1)