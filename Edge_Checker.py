a,b=map(int,input().split())
if(abs(b-a)==1):
    print("Yes")
elif(abs(a-b)==9):
    print("Yes")
else:
    print("No")