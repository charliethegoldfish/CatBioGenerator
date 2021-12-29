import random

# Eventually these will be filled from some text files
cat_names = ["Rufus", "Iggy", "Caramel", "Popcorn"]
cat_colours = ["black", "red", "aquamarine"]
cat_adjectives = ["fluffy", "sly", "bouncey", "graceful"]
cat_interests = ["hiking", "stealing snacks", "fetch", "standing in the shower"]

bio_structure = "{name} is a {adjective} {colour} cat who enjoys {activity_01} and {activity_02}"

# Function to read in files and store data

# Function to pick data to fill in bio with
def pick_element(list):
    index = random.randint(0, len(list)-1)
    return list[index]

# Function to construct bio
def construct_bio():
    name = pick_element(cat_names)
    colour = pick_element(cat_colours)
    adj = pick_element(cat_adjectives)
    activity_01 = pick_element(cat_interests)
    activity_02 = pick_element(cat_interests)

    return bio_structure.format(name=name, colour=colour, adjective=adj, activity_01=activity_01, activity_02=activity_02)

# Function to display bio (should this be combined with above function?)

# Function to take input
def display_greeting():
    print("Welcome to the Digital Cat Shelter. Would you like to read the bio for one of our cats? Y/N")
    answer = input()

    if answer.lower() == 'y':
        display_bio()
    else:
        print("Have a nice day!")

def display_bio():
    print("\n")
    print(construct_bio())
    print("\n")
    
    print("Would you like to view another bio? Y/N")
    answer = input()
    if answer.lower() == 'y':
        display_bio()
    else:
        print("Have a nice day!")

# Main code goes below here
display_greeting()