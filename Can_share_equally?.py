a,b=map(int,input().split())
if(a==b):
    print("YES")
elif((a!=0 and a%2==0) or  (a==0 and b%2==0)):
    print("YES")
else:
    print("NO")