a=int(input())
n=list(map(int,input().split()))
s=0
for i in n:
    s=s+i
c=s/len(n)
print(f"{c:.2f}")