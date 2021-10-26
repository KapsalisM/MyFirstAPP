
n=input("give number ")
while n <1 or n >30000:
    n=input("give number ")

K=[]
for i in range(2,n):
    K.append(i)

p=2
while p**3<n:
    for i in range(p-1,len(K)):
        if K[i]%p==0:
            K[i]=0
    p += 1
    while K[p-1] ==0:
        p+=1

for i in range(len(K)):
    if K[i]!=0:
        print K[i],"prwtoi arithmoi"
