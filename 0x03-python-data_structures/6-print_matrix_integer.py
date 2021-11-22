#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for x in range(len(matrix[i])):
            if x != 0:
                print(" ", end="")
            print("{:d}".format(matrix[i][x]), end="")
        print("")
