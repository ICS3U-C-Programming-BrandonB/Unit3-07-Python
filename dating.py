#!/usr/bin/env python3

# Created By: Brandon
# Date: October 30th, 2025
# This program asks the user for their age and determines if they can date the grandfathers grandchild.


def main():

    # get the age from the user
    user_age = input("Enter Your Age:  ")

    # Checking if the user entered an integer correctly
    try:
        user_age = int(user_age)
        print("You entered an age!")

        # determine whether or not the user age's in between the correct age
        if user_age >= 25 and user_age <= 40:
            print("You can date my grandchild")
        else:
            print(
                "You cannot date my grandchild, as you are {} years old".format(
                    user_age
                )
            )
    except ValueError:
        print("That is not a valid age")


# outputs the function
if __name__ == "__main__":
    main()
