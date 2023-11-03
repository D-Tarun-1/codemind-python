a,b=map(int,input().split())
ls=[]
s=0
for i in range(a):
    inner=list(map(int,input().split()))[:b:]
    ls.append(inner)
for inner in ls:
    for every in inner:
        s+=every
print(s)
        