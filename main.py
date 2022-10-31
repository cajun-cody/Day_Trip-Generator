
import random
my_destinations = ["Nola", "Breckenridge", "Boston", "Da Camp"]
my_restaurants = ["Marcello's", "Tap Room", "Frontier", "The Maggie"]
my_entertainment = ["Skiing", "Fishing", "Concert", "Sport Event"]
my_transportation = ["Jeep", "Boat", "Plane", "Motercycle"]

destination = random.choice(my_destinations)
restaurant = random.choice(my_restaurants)
entertainment = random.choice(my_entertainment)
transportation = random.choice(my_transportation)


def run_print_full_trip():
    print("Destination:" + " " + destination)
    print("Restaurant:" + " " + restaurant)
    print("Entertainment:" + " " + entertainment)
    print("Transportation:" + " " + transportation)

def select_random_item(current_list): #new randomize. Do I have the user choose from each list? Do I ask for each list?
    conf_bool = True
    while conf_bool:
        random_item = random.choice(current_list)
        user_input = input(f"{random_item} was selected, how does that sound(y/n)? ")
        if user_input == "y":
            return random_item
        else:
            random_item = input(f"{random_item} was selected, how does that sound? yes or no: ")
            return random_item

def confirm_trip(final_trip): #new confirm/satisfaction trip
    #put in final check + recall the function that created the original trip
    print(final_trip)
    confirm_bool = True
    while confirm_bool:
        user_input = input("How does that sound? ")
        if user_input == "no":
            #rereun the whole process

# add these to a funciton
def create_trip():
    destination = select_random_item(my_destinations)
    restaurant = select_random_item(my_entertainment)
    entertainment = select_random_item(my_entertainment)
    transportation = select_random_item(my_transportation)

def run_trip_satisfation():
    active = True
    while active:
        trip_satisfation = input("Are you satisfied with your trip? yes or no? ")
        if trip_satisfation == "yes":
            active = False
            print("Excellent! Here is your completed trip!")
            print("Destination:" + " " + destination)
            print("Restaurant:" + " " + restaurant)
            print("Entertainment:" + " " + entertainment)
            print("Transportation:" + " " + transportation)
        else:
            new_destination = random.choice(my_destinations) #error 
            new_restaurant = random.choice(my_restaurants)
            new_entertainment = random.choice(entertainment)
            new_transportation = random.choice(transportation)
            print("How about this one?")
            print("Destination:" + " " + new_destination)
            print("Restaurant:" + " " + new_restaurant)
            print("Entertainment:" + " " + new_entertainment)
            print("Transportation:" + " " + new_transportation)
run_trip_satisfation()     





def run_day_trip_generator():
    print_full_trip()
    trip_satisfation()

#run_day_trip_generator()  










