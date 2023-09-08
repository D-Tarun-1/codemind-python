def palin(a):
    s=0
    c=a
    while(a!=0):
        r=a%10
        s=s*10+r
        a//=10
    if(c==s):
        return True
    else:
        return False
a=int(input())
i=a
j=a
while True:
   i+=1
   if(palin(i)):
        break
while True:
    j-=1
    if(palin(j)):
        break
d1=a-j
d2=i-a
if(d1>d2):
    print(i)
elif(d1<d2):
    print(j)
else:
    print(j,i)
  