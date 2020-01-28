# (using __init__) function in this program



class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self):
        print("loool")
    
    def wide(self):
        print('lol')


point1=Point(12,14)


''' if we want to change the value of point1.x then
    add a line(point.x=123(or any thing ))'''

point1.x=14
print(point1.x)