def ex1(array):
    array_size = len(array)

    for i in range((array_size - 2) // 2 + 1):
        if (array[2 * i + 1] > array[i]):
            return False

        if (2 * i + 2 < array_size and array[2 * i + 2] > array[i]):
            return False
    return True


def ex2(array):
    heap_size = len(array) - 1
    for i in range((heap_size - 2) // 2 + 1, -1, -1):
        max_heapify(array, i, heap_size)

    print(array)


def max_heapify(array, i, heap_size):
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2

    if (left_child_index <= heap_size and array[left_child_index] > array[i]):
        largest_index = left_child_index
    else:
        largest_index = i

    if (right_child_index <= heap_size and array[right_child_index] > array[largest_index]):
        largest_index = right_child_index

    if (largest_index != i):
        array[largest_index], array[i] = array[i], array[largest_index]
        max_heapify(array, largest_index, heap_size)


def ex4(array1, array2):
    length1 = len(array1)
    length2 = len(array2)

    summed_length = length1 + length2

    result_array = []

    internal_pointer1 = 0
    internal_pointer2 = 0

    for i in range(summed_length + 1):
        if (length1 > internal_pointer1 and length2 > internal_pointer2):
            if (array1[internal_pointer1] < array2[internal_pointer2]):
                result_array.append(array1[internal_pointer1])
                internal_pointer1 += 1
            else:
                result_array.append(array2[internal_pointer2])
                internal_pointer2 += 1
        elif (length1 > internal_pointer1):
            result_array.append(array1[internal_pointer1])
            internal_pointer1 += 1
        elif (length2 > internal_pointer2):
            result_array.append(array2[internal_pointer2])
            internal_pointer2 += 1

    print(result_array)

if __name__ == '__main__':
    # Example proper heaps
    proper_heap = [33, 6, 12, 4, 6, 11]
    proper_heap2 = [9, 7, 8, 4, 2, 1, 7, 4]
    # Example not proper heaps
    not_proper_heap = [12, 6, 33, 4, 6, 11]
    not_proper_heap2 = [7, 2, 1, 4, 9, 8, 7, 4]
    # Exercise 1 arrays
    ex1_heap = [50, 9, 8, 7, 2, 1, 7, 4, 4]
    ex2_heap = [50, 9, 8, 7, 2, 1, 7, 4, 8]
    ex3_heap = [50, 9, 8, 7, 2, 1, 7, 4, 4, 2]
    # Exercise 4 arrays
    ex4_array1 = [1, 2, 8, 9]
    ex4_array2 = [1, 3, 5, 8, 10, 15, 18]
    # Exercise 1
    #print(ex1(ex3_heap))
    # Exercise 2
    #ex2(not_proper_heap2)
    # Exercise 4
    ex4(ex4_array1, ex4_array2)
