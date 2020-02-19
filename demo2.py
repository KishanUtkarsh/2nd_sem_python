N =input()
A=N.split()
B=[]
for i in A:
    if int(i)%5==0:
        continue
    B.append(i)

for i in B:
    print(i,end="")