import random as r
d1=[1,2,3,4,5,6]
d2=[1,2,3,4,5,6]

for i in range(1):
    x=r.choice(d1)
    for j in range(2):
        y=r.choice(d2)
        

print(f'({x},{y})')
print('({0},{1})'.format(x,y))