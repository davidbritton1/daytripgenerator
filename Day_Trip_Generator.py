import random


#Lists
destinations = ['California', 'Florida','Ohio']
resturants = ['Pizza Hut','McDonalds','Taco Bell']
transportation = ['Car','Train','Bike']
entertainment = ['Movie','Concert','Shopping']

#functions
def choose_destination():
    place = random.choice(destinations)
    print(place)
    destination = input(f'Welcome to the Day trip generator, we have selected {place} for your destination. Would you like to go to {place}? Enter y/n')
    if destination == 'n':
        print(f"Sorry you don't like that place, how about {place}? ")
    elif destination == 'y':
            print("Great! Let's move on.")


def choose_resturant():
    food = random.choice(resturants)
    print(food)
    resturants = input(f"We have selected {food} as a place to eat. Would you like to eat here? Enter y/n")
    pass

def choose_transportation():
    moving = random.choice(transportation)
    print(moving)
    
    pass

def choose_entertainment():
    watching = random.choice(entertainment)
    print(watching)
   
    pass


choose_destination()