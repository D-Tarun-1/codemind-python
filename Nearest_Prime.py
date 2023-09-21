def prime(n):
    if(n==1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
            break
    else:
        return True
b=int(input())
for i in range(1,b+1):
    a=int(input())
    i=a
    j=a
    while True:
        if(prime(i)):
           break 
        i+=1
    while True:
        j-=1
        if(prime(j)):
            break  
    c=abs(a-i)
    d=abs(a-j)
    if(c>d):
        print(j)
    elif(c<d):
        print(i)
    else:
        print(j)