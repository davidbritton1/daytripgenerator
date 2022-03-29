import random


#Lists
destinations = ['California', 'Florida','Ohio']
resturants = ['Pizza Hut','McDonalds','Taco Bell']
transportation = ['Car','Train','Bike']
entertainment = ['Movie','Concert','Shopping']

#functions
def choose_destination():
    place = random.choice(destinations)
    destination = input(f'Welcome to the Day trip generator, we have selected {place} for your destination. Would you like to go to {place}? Enter y/n')
    if destination == 'n':
        new_place = random.choice(destinations)
        print(f"Sorry you don't like that place, how about {new_place}? y/n")
    elif destination == 'y':
            print("Great! Let's move on.")
    else:
        print("I'm sorry please type. y/n")
    


def choose_resturant():
    food = random.choice(resturants)
    resturants = input(f"We have selected {food} as a place to eat. Would you like to eat here? Enter y/n")
    if resturants == 'n':
        print(f"Sorry you don't like that resturant. Would you like to go to {food}?")
    elif resturants == 'y':
        print("Great! Let's continue")

    pass

def choose_transportation():
    moving = random.choice(transportation)
    print(moving)
    transportation = input(f"We have chosen {transportation} as you mode of transportion")
    if transportation == 'n':
        print(f"Sorry you don't like that transportation")

def choose_entertainment():
    watching = random.choice(entertainment)
    print(watching)
   
    pass


choose_destination()