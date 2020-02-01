class Animals:
    def foots(self):
        print('four Legs')

    def eye(self):
        print('beautiful Eyes')


class Animals1:
    def tail(self):
        print('big and beautifull tails')


class Ankit(Animals,Animals1):
    pass



dog=Ankit()
dog.tail()
dog.eye()