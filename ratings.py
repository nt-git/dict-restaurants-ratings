"""Restaurant rating lister."""
import sys


def user_input():
    """Takes in user input for restaurant and it's rating, append to dictionary, and returning update dictionary"""
        
    restaurant_name_input = raw_input("Enter Restaurant name: ")
    while True:
        restaurant_score_input = int(raw_input("Enter Restaurant's rating: "))
        if 0 <= restaurant_score_input <= 5:
            return restaurant_name_input, restaurant_score_input
        else:
            print "Please Enter Valid Input"



def restaurant_rating(filename):
    """Takes in a file, reads the restaurant and it's ratings, and stores them in a dictionary"""

    rating_file = open(filename)

    restaurant_ratings = {}

    for line in rating_file:
        line = line.rstrip()
        restaurant_name, rating = line.split(":")

        restaurant_ratings[restaurant_name] = rating

    # for restaurant, number in sorted(restaurant_ratings.items()):
    #     print "{} is rated at {}".format(restaurant, number)



    # restaurant_name_input, restaurant_score_input = user_input()
    # restaurant_ratings[restaurant_name_input] = restaurant_score_input

    for restaurant, number in sorted(restaurant_ratings.items()):
        print "{} is rated at {}".format(restaurant, number)


def user_choice():
    """Giving user options to see restaurant ratings, adding a new restaurant, or quitting"""

    OPTIONS = """
        a) See ratings
        b) Add rating
        c) Quit
    """

    while True:
        print OPTIONS
        user_choice = raw_input("What would you like to do?: ")

        if user_choice == "a":
            restaurant_rating(filename)
        elif user_choice == "b":
            user_input()
        elif user_choice == "c":
            print "Good-bye!"
            break
        else:
            print "Invalid input"


filename = "scores.txt"
# for text_file in sys.argv[1:]:
#     restaurant_rating(text_file)



## all functions work, except dictionary doesn't get updated with user input
# FIX IT