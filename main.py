
import random

my_destinations = ["Nola", "Breckenridge", "Boston", "Da Camp"]
my_restaurants = ["Marcello's", "Tap Room", "Frontier", "The Maggie"]
my_entertainment = ["Skiing", "Fishing", "Concert", "Sport Event"]
my_transportation = ["Jeep", "Boat", "Plane", "Motercycle"]

destination = random.choice(my_destinations)
restaurant = random.choice(my_restaurants)
entertainment = random.choice(my_entertainment)
transportation = random.choice(my_transportation)


def print_full_trip():
    print("Destination:" + " " + destination)
    print("Restaurant:" + " " + restaurant)
    print("Entertainment:" + " " + entertainment)
    print("Transportation:" + " " + transportation)

def run_day_trip_generator():
    print_full_trip()


print("Here are some ideas for a trip you can take.")
run_day_trip_generator()  

active = True
while active:
    message = input("Are you satisfied with your trip? yes or no ")
    if message == "yes":
        active = False
        print("Here is your completed trip!")
        print("Destination:" + " " + destination)
        print("Destination:" + " " + restaurant)
        print("Destination:" + " " + entertainment)
        print("Destination:" + " " + transportation)
     



