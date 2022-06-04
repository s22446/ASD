def fibonnaci(amount):
    first, second = 0, 1

    for i in range(0, amount):
        first, second = second, first + second

    print(first)