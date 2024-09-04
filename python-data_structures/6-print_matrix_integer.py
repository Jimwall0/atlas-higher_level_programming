#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for call in range(len(matrix)):
        for index in range(len(matrix[call])):
            string = "{:d}"
            a = len(matrix[call]) - 1
            print(string.format(matrix[call][index]), end=" " if index != a else "")
        print()
