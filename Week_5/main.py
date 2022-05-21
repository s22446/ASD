# IMPORTS
import factorial.factorial as factorial
import binary_search.binary_search as bs
import sum_3.sum_3 as sum3
import reverse.reverse as reverser

if __name__ == '__main__':
    # FACTORIAL
    print("FACTIORIAL: ", factorial.calculate_factorial(8))
    # BINARY SEARCH
    #                      0  1  2  3  4   5   6    7    8    9   10   11    12
    binary_search_array = [0, 1, 2, 4, 6, 19, 25, 100, 200, 300, 400, 600, 1000]
    print("BINARY SEARCH: ", bs.start_search(binary_search_array, 10000))
    # SUM3
    print("SUM 3: ", sum3.sum_3(15))
    # REVERSE WORD
    word = "kot"
    print("REVERSED WORD (", word, "): ")
    reverser.reverse(word)
