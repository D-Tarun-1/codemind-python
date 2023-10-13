a=int(input())
n=list(map(int,input().split()))
s=0
for i in n:
    s=s+i
c=s//len(n)
if c in n:
    print(True)
else:
    print(False)