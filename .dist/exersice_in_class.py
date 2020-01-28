class Person:
    def __init__(self,name):
        self.name=name


    def talk(self):
        print(f'\nHii I am {self.name}.')



kishan=Person('kishan utkarsh')
kishan.talk()
 
bob=Person("bob")
bob.talk()