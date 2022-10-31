
import random

my_destinations = ["Nola", "Breckenridge", "Boston", "Da Camp"]
my_restaurants = ["Marcello's", "The Tap Room", "Frontier", "The Maggie"]
my_entertainment = ["Skiing", "Fishing", "Concert", "Sport Event"]
my_transportation = ["Jeep", "Boat", "Plane", "Motercycle"]

def select_random_item(current_list): 
    conf_bool = True
    while conf_bool == True:
        random_item = random.choice(current_list)
        user_input = input(f"{random_item} was selected, how does that sound(y/n)? ")
        if user_input == "y":
            conf_bool = False
            selected_item = random_item
            return selected_item
        else:
            return select_random_item(current_list)

def run_confirm_my_trip():
    active = True
    while active == True:
        
        confirmed_trip = input("Are you satisfied with this trip (y/n)? ")
        if confirmed_trip == "y":
            active = False
            print("Your trip is complete!")
            print("You are going to"+ " " + chosen_dest)
            print("You will be eating at" + " " + chosen_rest)
            print("For enjoyment you can enjoy" + " " + chosen_entertainment)
            print("You will get there by" + " " + chosen_trans)
        else:
            return select_random_item()   


chosen_dest = select_random_item(my_destinations)
chosen_rest = select_random_item(my_restaurants)
chosen_entertainment = select_random_item(my_entertainment)
chosen_trans = select_random_item(my_transportation)
print("Your chosen destination is" + " " + chosen_dest)
print("Your chosen restaurant is" + " " + chosen_rest)
print("Your chosen entertainment is" + " " + chosen_entertainment)
print("Your chosen transportation is by" + " " + chosen_trans)
print()

run_confirm_my_trip()









