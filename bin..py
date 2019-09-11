n=int(input())
c=bin(n)
s=str(c)
print(len(s.replace("0b","")))
