def zad_1():
    exercise1_array = [7, 5, 3, 2, 15, 126, 1, 502]

    for i in range(1, len(exercise1_array)):
        key = exercise1_array[i]
        j = i - 1
        while j > -1 and exercise1_array[j] > key:
            exercise1_array[j + 1] = exercise1_array[j]
            j = j - 1
        exercise1_array[j + 1] = key

    print(exercise1_array)

def zad_2():
    exercise2_array = [7, 5, 3, 2, 15, 126, 1, 502]
    n = len(exercise2_array)

    while n > 1:
        condition = True

        for i in range(0, n - 1):
            if exercise2_array[i] > exercise2_array[i + 1]:
                temp = exercise2_array[i + 1]
                exercise2_array[i + 1] = exercise2_array[i]
                exercise2_array[i] = temp
                condition = False

        if condition:
            break
        n = n - 1
    print(exercise2_array)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    zad_1()
    zad_2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
