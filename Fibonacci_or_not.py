a=int(input())
b=0
c=1
s=0
flag=0
for i in range(1,a-1):
    s=b+c
    b=c
    c=s
    if(a==s):
        flag=1
        break
if(flag==1):
    print("True")
else:
    print("False")