n=int(input())
v=[]
a=1
while a**3<=n:
    v.append(a**3)
    a+=1
print(*v)
