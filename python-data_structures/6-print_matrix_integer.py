#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for call in range(len(matrix)):
        for index in range(len(matrix[call])):
            string = "{:d} "
            print(string.format(matrix[call][index]), end="")
        print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
