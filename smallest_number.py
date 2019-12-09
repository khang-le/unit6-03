#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Dec 2019
# This program uses a list as a parameter

import random


def sum_of_numbers(list_of_numbers):
    # this functions find the smallest value

    total_smallest = 100

    for counter in list_of_numbers:
        if total_smallest > counter:
            total_smallest = counter
    return total_smallest


def main():
    # this function uses a list

    random_numbers = []

    # input
    print("The numbers are: ")
    for loop_counter in range(0, 4):
        a_single_number = random.randint(0, 5)
        random_numbers.append(a_single_number)
        print("{0} ".format(random_numbers[loop_counter]), end="")
        print("")
    smallest = sum_of_numbers(random_numbers)
    print("The smallest number is: {0}".format(smallest))


if __name__ == "__main__":
    main()
