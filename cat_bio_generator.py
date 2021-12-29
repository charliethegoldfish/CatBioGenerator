import random

# File names
names_fname = "cat_names.txt"
adjectives_fname = "cat_adjectives.txt"
colours_fname = "cat_colours.txt"
interests_fname = "cat_interests.txt"

# Eventually these will be filled from some text files
cat_names = []
cat_colours = []
cat_adjectives = []
cat_interests = []

bio_structure = "{name} is a {adjective} {colour} cat who enjoys {activity_01} and {activity_02}"

# Function to read in files and store data
def parse_file_into_list(file_name, list):
    file = open(file_name, "r")

    for line in file:
        line_stripped = line.strip('\n')
        list.append(line_stripped)

    # print(list)
    file.close()

def parse_files():
    # Could make a dictionary of filenames? Then loop through that to tidy this up
    parse_file_into_list(names_fname, cat_names)
    parse_file_into_list(colours_fname, cat_colours)
    parse_file_into_list(adjectives_fname, cat_adjectives)
    parse_file_into_list(interests_fname, cat_interests)

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
parse_files()
display_greeting()