n = int(input())
L = [int(x) for x in input().split()]
q = int(input())
for i in range(q) :
    L2 = [int(x) for x in input().split()]
    if L2[0]==1 :
        _,a,b,x = L2
        for j in range(a,b+1) :
            L[j] += x
    elif L2[0]==2 :
        _, a, b = L2
        max1 = max(L[a:b+1])
print(max1,end='')

