
i=1
started=False
while (i>0):
    car =input('>')
    if 'help'==car.lower():
        print('start - to start the car\nstop - to stop the car\nquit - to exit')
    elif 'start'==car.lower():
        if started:
            print('car is already started..')
        else:
            started=True
            print("car started....ready to go")    

    elif 'stop'==car.lower():
        if not started:
            print('car already stopped')
        else:
            started=False   
            print("car stopped.")

    elif 'quit'==car.lower():
        break
    else:
        print("i don't understand that..")



