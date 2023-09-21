def prime(n):
    if(n==1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True
a=int(input())
flag=0
for i in range(2,a+1):
    if prime(i):
        for j in range(2,i+1):
            if prime(j):
                if a==i*j:
                    c=i
                    d=j
                    flag=1
                    break
if(flag==1):
    print(d,c)
else:
    print("-1")