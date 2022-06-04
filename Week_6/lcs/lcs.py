def lcs(seq1, seq2):
    seq1_length = len(seq1)
    seq2_length = len(seq2)
    matrix_numbers = [[0 for x in range(seq1_length + 1)] for y in range(seq2_length + 1)]
    matrix_directions = [["0 " for x in range(seq1_length + 1)] for y in range(seq2_length + 1)]

    for i in range(1, seq1_length + 1):
        for j in range(1, seq2_length + 1):
            if (seq1[i - 1] == seq2[j - 1]):
                matrix_numbers[i][j] = matrix_numbers[i - 1][j - 1] + 1
                matrix_directions[i][j] = "\\"
            else:
                if (matrix_numbers[i - 1][j] >= matrix_numbers[i][j - 1]):
                    matrix_numbers[i][j] = matrix_numbers[i - 1][j]
                    matrix_directions[i][j] = "|"
                else:
                    matrix_numbers[i][j] = matrix_numbers[i][j - 1]
                    matrix_directions[i][j] = "-"

    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matrix_numbers]))
    print("\n")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matrix_directions]))
