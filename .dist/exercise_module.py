def find_greater(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number>maximum:
            maximum=number

    return maximum

        
