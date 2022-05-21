def calculate_factorial(number):
    if number == 1:
        return number
    else:
        return number * calculate_factorial(number - 1)