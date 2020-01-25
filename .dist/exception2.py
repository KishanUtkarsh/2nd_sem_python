try:
    age=int(input('age>'))
    income=2000
    risk=income/age
    print(age)

except ZeroDivisionError:
  print('Age can not be zero')

except ValueError:
    print('invalid value')