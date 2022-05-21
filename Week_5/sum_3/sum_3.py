def sum_3(number):
    if (number == 0):
        return 0
    elif (number % 3 == 0):
        return number + sum_3(number - 3)
    else:
        return 0 + sum_3(number - 1)