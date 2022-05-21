def start_search(array, number):
    if (array[0] == number):
        return 0
    elif (array[len(array) - 1] == number):
        return len(array) - 1
    else:
        return search(array, 0, len(array) - 1, number)

def search(array, start, end, number):
    if end >= start:
        middle = (start + end) // 2

        if (array[middle] == number):
            return middle
        elif (array[middle] > number):
            return search(array, start, middle - 1, number)
        else:
            return search(array, middle + 1, end, number)
    else:
        return "Not found"
