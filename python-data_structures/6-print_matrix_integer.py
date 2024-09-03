#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for call in range(len(matrix)):
        for index in range(len(matrix[call])):
            string = "{:d}"
            print(string.format(matrix[call][index]), end=" " if index != 2 else "")
        print()
