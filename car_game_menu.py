
i=1
while (i>0):
    car =input()
    if 'help'==car.lower():
        print('start - to start the car\nstop - to stop the car\nquit - to exit')
    elif 'start'==car.lower():
        print('car started....ready to go')
    elif 'stop'==car.lower():
        print('car stopped.')
    elif 'quit'==car.lower():
        break
    else:
        print("i don't understand that..")

