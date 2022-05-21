import array as arr

def quicksort(given_array, start_index, end_index):
    if (start_index < end_index):
        q = partition(given_array, start_index, end_index)
        quicksort(given_array, start_index, q - 1)
        quicksort(given_array, q + 1, end_index)


def partition(given_array, start_index, end_index):
    x = given_array[end_index]
    i = start_index - 1

    for j in range(start_index, end_index):
        if (given_array[j] <= x):
            i += 1
            given_array[i], given_array[j] = given_array[j], given_array[i]
    given_array[i + 1], given_array[end_index] = given_array[end_index], given_array[i + 1]

    return i + 1


def break_array(given_array):
    for i in range(1, len(given_array), 2):
        given_array[i], given_array[i - 1] = given_array[i - 1], given_array[i]


def exercise3(given_array):
    pointer = 0
    for i in range(0, len(given_array)):
        if (given_array[i] > 0):
            element = given_array[i]
            given_array.pop(i)
            given_array.insert(pointer, element)
            pointer += 1


def merge_sort(given_array):
    if len(given_array) > 1:
        mid = len(given_array) // 2
        left_array = given_array[:mid]
        right_array = given_array[mid:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                given_array[k] = left_array[i]
                i += 1
            else:
                given_array[k] = right_array[j]
                j += 1

            k += 1

        while i < len(left_array):
            given_array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            given_array[k] = right_array[j]
            j += 1
            k += 1

if __name__ == '__main__':
    # Example arrays
    array = [7, 14, 24, 1, 5, 18, 9]
    array2 = [12, 7, 3, 8, 15, 3, 8, 12, 21]
    array3 = [5, 12, 21, 7, 5, 5, 13, 4, 2, 12, 13]
    exercise3_array = [5, 10, -25, 9, -14, -6, 2, -1]
    # Copied array for sort
    sort_array = array
    merge_array = array2
    # Setting arguments
    start_argument = 0
    end_argument = len(sort_array) - 1
    # Calling quicksort
    quicksort(sort_array, start_argument, end_argument)

    print('After quicksort:')
    print(sort_array)

    break_array(sort_array)
    print('Broken array:')
    print(sort_array)

    exercise3(exercise3_array)
    print('Exercise 3:')
    print(exercise3_array)

    merge_sort(merge_array)
    print('Merge sort:')
    print(merge_array)
