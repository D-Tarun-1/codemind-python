def happy(a):
    while True:
        if(a==1 or a==7):
            return True
        elif(a<10):
            return False
        s=0
        while(a!=0):
            r=a%10
            s=s+(r*r)
            a//=10
        a=s
a=int(input())
ishappy=happy(a)
if(ishappy):
    print("True")
else:
    print("False")