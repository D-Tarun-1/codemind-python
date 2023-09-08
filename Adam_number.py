a=int(input())
s1=0
sq=a*a
b=a
while(a!=0):
    r1=a%10
    s1=s1*10+r1
    a//=10
w=s1*s1
s=0
e=sq
while(w!=0):
    r=w%10
    s=s*10+r
    w//=10
if(s==sq):# and sq==s):
    print("True")
else:
    print("False")
    