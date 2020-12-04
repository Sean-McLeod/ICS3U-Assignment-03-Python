#!/usr/bin/env python3

# Created by Sean McLeod
# Created on December 2020
# This program can tell the user if their age is eligible to vote

import constants


def main():
    # this function can tell the user if they are eligible to vote

    print("This program will tell you if you are eligible to vote")

    # input
    age = int(input("Please type in your age: "))
    print("")

    # process & output
    if age >= constants.ELIGIBLE_AGE:
        print("You are eligible to vote!")
    else:
        print("Sorry, you are not eligible")


if __name__ == "__main__":
    main()
