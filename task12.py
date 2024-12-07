a = int(input())
k = 0
m=[]
for i in range(2,a):
    if k < 5 and a % i == 0:
        print(a // i)
        k+=1
        m.append(a//i)
    if k == 5: break
if k == 5: print(a//i)
else: print(0)