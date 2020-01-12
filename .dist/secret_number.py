secret_number =5
i=1
while (i<=3):
    s=int(input("enter the secret number : "))
    if s==secret_number:
        print ('you win')
        break
    i+=1
    
    
else:   
    print("you lose")
