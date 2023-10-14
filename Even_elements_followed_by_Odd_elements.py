a=int(input())
n=list(map(int,input().split()))
for i in n:
    if(i%2==0):
        print(i,end=" ")
for i in n:
    if(i%2!=0):
        print(i,end=" ")
