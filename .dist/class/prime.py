for i in range (1,100):
    count=0
    for j in range(2,(i//2+1)):
        n=j
        if (i%j==0):
            count=count+1
            break
    if i!=1 and count==0:
        print(i)