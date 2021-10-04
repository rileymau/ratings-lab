"""Restaurant rating lister."""
import sys

input_file = open(sys.argv[1])

def print_rating():
    rating_dict = {}
    for line in input_file:
        name, rating = line.rstrip().split(":")
        rating_dict[name] = rating

    sorted_dict = sorted(rating_dict.keys())
    for key in sorted_dict: 
        print(f"{key} is rated at {rating_dict[key]}")
    return

while True:
    print("what would you like to do ?")
    print("Seeing all the ratings in alphabetical order?")
    print("Adding a new restaurant?")
    print("Quitting?")
    print("Please enter S, A, or Q")
    response = input()
    
    if response == 'Q':
        break
    elif response == "S":
        print_rating()
    elif response == "A":
        restaurant_name = input("What is the restraunt name? ")
        restaurant_rating = input("What is their rating? Choose an integer between 1 and 5. ")
        if 5 < int(restaurant_rating) < 1:
           input("Please re-enter the rating !\n")
        #else:
            #print_rating()
            #rating_dict[restaurant_name] = int(restaurant_rating)




input_file.close()


