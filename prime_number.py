def prime(n):
    if(n==1):
        print("not a prime")
    for i in range(2,n):
        if(n%i==0):
            print("not a prime")
            break
    else:
        print("prime")
a=int(input())
prime(a)