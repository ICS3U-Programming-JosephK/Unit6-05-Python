#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: December 21
# This calculate the average of user input

import random

# Defining the function that calculates the average
def calc_average(list):
    total_sum = 0
    # gets the length of the list, number of indexes
    divisor = len(list)
    for a_num in list:
        total_sum += a_num
    average = total_sum / divisor
    return average


def main():
    # Creating empty list
    nums = []
    while True:
        # Get user input
        user_input = input("Enter a mark: ")

        if user_input == "-1":
            break
        else:
            try:
                user_int = int(user_input)
                nums.append(user_int)
            except:
                print("Invalid input. Please enter a real number or -1")

    # Calling the function, after the loop breaks, goes straight to here
    average = calc_average(nums)

    # Displaying the average
    print()
    print("The average is {}".format(average))


if __name__ == "__main__":
    main()
