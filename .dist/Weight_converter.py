unit=input("what is your weight?\n ")
measurement=input ("Enter P for pound and K for kilogram : ")
if measurement=='k':
    
    weight=int(unit)/0.45
    print(f"{weight} in pound")
else:
    weight=0.45*int(unit)
    print(f"{weight} in kg ")
