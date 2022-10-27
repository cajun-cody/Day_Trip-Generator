
import random

#(5 points): As a developer, I want to make at least three commits with descriptive messages.

#(5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists. Check

#(5 points): As a user, I want a destination to be randomly selected for my day trip. Check

#(5 points): As a user, I want a restaurant to be randomly selected for my day trip. Check

#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. Check

#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. Check

#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

#(10 points): As a user, I want to display my completed trip in the console.

#(5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

my_destinations = ["Nola", "Breckenridge", "Boston", "Da Camp"]
my_restaurants = ["Marcello's", "Tap Room", "Frontier", "The Maggie"]
my_entertainment = ["Skiing", "Fishing", "Concert", "Sport Event"]
my_transportation = ["Jeep", "Boat", "Plane", "Motercycle"]

def run_day_trip_generator():
    
    my_destinations = ["Nola", "Breckenridge", "Boston", "Da Camp"]
    print(random.choice(my_destinations))

    my_restaurants = ["Marcello's", "Tap Room", "Frontier", "The Maggie"]
    print(random.choice(my_restaurants))

    my_entertainment = ["Skiing", "Fishing", "Concert", "Sport Event"]
    print(random.choice(my_entertainment))

    my_transportation = ["Jeep", "Boat", "Plane", "Motercycle"]
    print(random.choice(my_transportation))

print("Here are some ideas for a trip you can take.")
run_day_trip_generator()

active = True
while active:
    message = input("Are you satisfied with your trip? ")
    if message == "yes":
        active = False
        print("Here is my completed trip!")
        print(f"Destination:" + " " + random.choice(my_destinations)) 



